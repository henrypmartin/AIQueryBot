'''
@author: henry Martin
'''
import logging
import mysql.connector

logger = logging.getLogger(__name__)
from com.querybot import config_reader

logger = logging.getLogger(__name__)

def get_db_connection():
    try:
        logger.info(f'Getting DB connection for {config_reader.get_property("mysql.organization", "db_url")}')
        # Connect to MySQL database
        conn = mysql.connector.connect(
            host=config_reader.get_property('mysql.organization', 'db_url'), 
            user=config_reader.get_property('mysql.organization', 'username'),
            password=config_reader.get_property('mysql.organization', 'password'),
            database=config_reader.get_property('mysql.organization', 'db_name')  
        )
        
    except mysql.connector.Error as err:
        print(f'Error is {err.msg}')
        raise err
    
    return conn
        
# Function to get database schema from MySQL
def get_database_schema():
    schema_info = ""
    try:
        # Connect to MySQL database
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Get all table names
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        
        # For each table, get column details
        for (table_name,) in tables:
            table_name = table_name.decode('utf-8')
            schema_info += f"Table: {table_name}\nColumns: "
            cursor.execute(f"SHOW COLUMNS FROM {table_name}")
            columns = cursor.fetchall()
            schema_info += ", ".join([column[0] for column in columns]) + "\n"

        cursor.close()
        conn.close()

    except mysql.connector.Error as err:
        logger.error(f'Error getting data from DB: {err.msg}')
        return f"Error: {err}"

    logger.debug(f'DB schema is : {schema_info}')
    return schema_info

def execute_sql_query(sql_query):
    logger.info(f"Executing query in organizations DB:\n{sql_query}")
    try:
        # Connect to MySQL database
        conn = get_db_connection()
        cursor = conn.cursor()

        # Execute the SQL query
        cursor.execute(sql_query)
        results = cursor.fetchall()

        # Fetch column names
        column_names = [i[0] for i in cursor.description]

        # Convert the result into a list of dictionaries (for easier JSON formatting)
        data = [dict(zip(column_names, row)) for row in results]

        cursor.close()
        conn.close()

        return data

    except mysql.connector.Error as err:
        logger.error(f'Error is {err.msg}')
        return f"Error: {err}"
    
if __name__ == "__main__":
    get_database_schema()