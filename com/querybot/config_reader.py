'''

@author: Henry Martin
'''

import configparser
import os

# Create a ConfigParser object
config = configparser.ConfigParser()
    
def load_config(config_file_path: str):

    print(f" Config fle path: {config_file_path}")
    
    # Read the properties file
    config.read(config_file_path)
        
def get_property(section, key):
    return config[section][key]

print(f'dir:{os.path.dirname(__file__)}')
config_file_path = os.path.join(os.path.dirname(__file__), "../../", "config.properties")
print(f'Config file path:{config_file_path}. Exists? {os.path.exists(config_file_path)}')
    
load_config(config_file_path)
