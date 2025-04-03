# Introduction

A simple yet powerful example of one of many GenAI capabilities querying relational database in natural language.

In this sample I'll showcase the use of Agentic RAG based approach, dealing with 2 different databases and depending on the context from user input how it meticulously executes query against correct database.

We have setup 2 databases *organization* and *CollegeDB*. The schema for both these databases can be found in the source code under *db_schema* dir.

The app will read user queries in natural language eg *list all employees working in HR department* or *instructor with max number of students enrolled for a course*
The

The system will interpret the user query and invoke correct agent to execute based on the context from the query.

There are 2 types of agents specified viz schema generation and query execution (for *organization* and *CollegeDB* each).

At first, the system will invoke the schema generation agent to generate the schema for the correct database as interpreted from the user query.
It'll then generate the SQL query using the schema and original user query as context, execute the query and return the response.

At the core of it is OpenAI "gpt-4o" Large Language Model (LLM).

Solution is implemented in Python for backend service, MySQL as relational database source, Strealit for UI and langgraph and langchain-openai for GenAI related libraries.

# Pre-requisite

1. Create MySQL databases *organization* and *CollegeDB* using given schema
2. Edit the config.properties file
 - log_file_path -> add the path to the log file where logs will be generated
 - openai -> add your OpenAI key
 - db_url, username, password and db_name -> your databse details for organization as well as college database

# Details
**querybot_start_up.py** is the main entry point. It launches a simple screen as below.
![image](https://github.com/user-attachments/assets/fa4c6fe7-a5b0-4432-9320-43db99cf32cd)

**querybot_service.py** is the main service where the LLM and Agents are initialized, user input passed to agent and sends the response back to the UI process.
It also maintains the history of conversation.

**db_agents.py** lists various agents viz schema generation and query execution agent for each of *organization* and *CollegeDB* databases

**querybot_prompts.py** simple yet effective prompt. For more advance scenarios, effective prompt engineering techniques can be used.
