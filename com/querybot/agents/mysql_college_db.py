'''
@author: henry Martin
'''
import logging
from com.querybot.utils.db_utils import get_database_schema, execute_sql_query

logger = logging.getLogger(__name__)
        
# Function to get database schema from MySQL
def get_college_database_schema():
    
    logger.debug('Getting DB schema for CollegeDB')
    return get_database_schema('mysql.college')

def execute_college_db_sql_query(sql_query):
    
    logger.info("Executing query in CollegeDB")
    
    return execute_sql_query(sql_query, 'mysql.college')
        
if __name__ == "__main__":
    get_database_schema()