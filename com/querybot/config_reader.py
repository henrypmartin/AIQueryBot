'''

@author: Henry Martin
'''

import configparser


# Create a ConfigParser object
config = configparser.ConfigParser()

def load_config(config_file_path: str):

    print(f" Config fle path: {config_file_path}")
    
    # Read the properties file
    config.read(config_file_path)
        
def get_property(section, key):
    return config[section][key]