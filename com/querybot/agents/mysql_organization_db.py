'''
@author: henry Martin
'''
import logging

logger = logging.getLogger(__name__)
from com.querybot import config_reader

# Function to get database schema from MySQL
def get_database_schema():
    schema_info = ""
    try:
        # Connect to MySQL database
        conn = mysql.connector.connect(
            host=config_reader.get_property('mysql.organization', 'db_url'), 
            user=config_reader.get_property('mysql.organization', 'username'),
            password=config_reader.get_property('mysql.organization', 'password'),
            database=config_reader.get_property('mysql.organization', 'db_name')  
        )
        cursor = conn.cursor()

        # Get all table names
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()

        # For each table, get column details
        for (table_name,) in tables:
            schema_info += f"Table: {table_name}\nColumns: "
            cursor.execute(f"SHOW COLUMNS FROM {table_name}")
            columns = cursor.fetchall()
            schema_info += ", ".join([column[0] for column in columns]) + "\n"

        cursor.close()
        conn.close()

    except mysql.connector.Error as err:
        return f"Error: {err}"

    return schema_info