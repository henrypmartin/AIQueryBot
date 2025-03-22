'''

@author: Henry Martin
'''
import logging
import traceback

from langchain_core.messages import AIMessage, HumanMessage, ToolMessage
from langchain_core.messages import RemoveMessage
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.prebuilt import create_react_agent

from com.querybot.agents.db_agents import mysql_organization_db_scheme_generation_agent, mysql_college_db_scheme_generation_agent, mysql_organization_db_query_execution_agent, \
                        mysql_college_db_query_execution_agent
from com.querybot.agents.querybot_prompts import output_formatter_prompt_template


logger = logging.getLogger(__name__)

memory = InMemorySaver()
llm = None
agent_executor = None

def initialize_querybot_service():
    global llm
    global agent_executor
    
    llm = ChatOpenAI(model="gpt-4o", temperature=0.1)
    
    tools = [mysql_organization_db_scheme_generation_agent, mysql_college_db_scheme_generation_agent, mysql_organization_db_query_execution_agent, mysql_college_db_query_execution_agent]
    
    agent_executor = create_react_agent(llm, tools, state_modifier=output_formatter_prompt_template, checkpointer=memory, debug=True)

def generate_response(query, session_id):
    
    config = {"configurable": {"thread_id": session_id}}
    
    if "messages" in agent_executor.get_state(config).values:
        hist_messages = agent_executor.get_state(config).values["messages"]
        logger.info(f'messages in memory {len(hist_messages)}')
        
        msgs_to_delete = []
        for msg in hist_messages:
            if not isinstance(msg, ToolMessage):
                msgs_to_delete.append(RemoveMessage(id=msg.id))
    
    mem_state = memory.get(config=config)
    
    chat_hist = []
    if mem_state:
        mem_messages = mem_state['channel_values']['messages']
        for msg in mem_messages:
            if not isinstance(msg, ToolMessage) and msg.content:
                chat_hist.append({msg.__class__.__name__:msg.content})
                
    logger.info(f"Query: {query}, userid: {session_id}")
    
    final_output = 'Unable to retrieve data at this moment, please try again later.'
    try:
        response = agent_executor.invoke({"messages": query}, config=config)
    
        logger.debug(f'Agent response is: {response}')
        ai_response = []
        
        for aimsg in response["messages"]:
            if isinstance(aimsg, HumanMessage):
                ai_response.clear()
                
            if isinstance(aimsg, AIMessage) and aimsg.content:
                ai_response.append(aimsg.content)            
        
        final_output = '\n'.join(ai_response)
    except:
        logger.error(f"Error occurred while processing request: {traceback.format_exc()}")

    logger.info(f"AIQueryBot Results:{final_output}")
       
    return final_output

