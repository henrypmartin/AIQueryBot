'''
Created on 2 Apr 2025

@author: henry
'''
import streamlit as st
import secrets
import os
from com.querybot.querybot_service import generate_response,\
    initialize_querybot_service
from com.querybot import config_reader
from logging.handlers import RotatingFileHandler
import logging

def initialize_logger():
    log_file_path = config_reader.get_property('local', 'log_file_path')

    handler = RotatingFileHandler(log_file_path, mode='w', maxBytes=5000000, backupCount=5, encoding='utf-8')
    
    logging.basicConfig(handlers=[handler],
                        level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s'
                        )
    
    logger = logging.getLogger(__name__)
    
def load_query_bot_ui():
    
    os.environ["OPENAI_API_KEY"] = config_reader.get_property('keys', 'openai')
    
    initialize_querybot_service()
    
    st.set_page_config(
        page_title="AI DB Query Bot",
        layout="wide"
    )
    
    if "chathistory" not in st.session_state:
        st.session_state.chathistory = []

    if "session_id" not in st.session_state:
        st.session_state.session_id = secrets.token_urlsafe(5)
        
    # Display chat messages
    for message in st.session_state.chathistory:
        with st.chat_message(message["role"]):
            st.markdown(message["text"])

    # Chat input
    if input_text := st.chat_input("How can I help you?"):
        # Add user message to chat history
        st.session_state.chathistory.append({"role": "user", "text": input_text})
        
        # Display user message
        with st.chat_message("user"):
            st.markdown(input_text)

        # Generate response
        with st.chat_message("assistant"):
            with st.spinner("Fetching response..."):
                chat_response = generate_response(input_text, st.session_state.session_id)
                st.markdown(chat_response)        
                # Add assistant response to chat history
                st.session_state.chathistory.append({"role": "assistant", "text": chat_response})


if __name__ == "__main__":
    initialize_logger()
    load_query_bot_ui()