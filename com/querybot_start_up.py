'''

@author: Henry Martin
'''

import logging
from logging.handlers import RotatingFileHandler
import os
import subprocess

from com.querybot import config_reader
from com.querybot.querybot_service import generate_response,\
    initialize_querybot_service
import datetime
import shutil

def backup_log_file(log_filepath):
    """Backs up the log file if it exists."""
    if os.path.exists(log_filepath):
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_filepath = f"{log_filepath}.{timestamp}"
        shutil.move(log_filepath, backup_filepath)
        print(f"Log file backed up to: {backup_filepath}")
    else:
        print("No existing log file to backup.")
        
def run_query_bot_cmd():
    log_file_path = config_reader.get_property('local', 'log_file_path')

    backup_log_file(log_file_path)
    
    handler = RotatingFileHandler(log_file_path, mode='w', maxBytes=5000000, backupCount=5, encoding='utf-8')
    
    logging.basicConfig(handlers=[handler],
                        level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s'
                        )
    
    logger = logging.getLogger(__name__)
    
    logger.info("Starting the app")
    
    os.environ["OPENAI_API_KEY"] = config_reader.get_property('keys', 'openai')
    
    initialize_querybot_service()
    
    while True:
        query = input("Ask anything related to any database:")
        response = generate_response(query, "1")
        
        print(f'Query is: {response}')

def run_query_bot_ui():
    log_file_path = config_reader.get_property('local', 'log_file_path')

    backup_log_file(log_file_path)
    
    handler = RotatingFileHandler(log_file_path, mode='w', maxBytes=5000000, backupCount=5, encoding='utf-8')
    
    logging.basicConfig(handlers=[handler],
                        level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s'
                        )
    
    logger = logging.getLogger(__name__)
    
    logger.info("Starting the app")
    
    file_path = os.path.join(os.path.dirname(__file__), "querybot", "querybot_ui.py")
    
    process = subprocess.Popen(["streamlit", "run", file_path])

def main():
    
    run_query_bot_ui()
    
if __name__ == "__main__":
    main()