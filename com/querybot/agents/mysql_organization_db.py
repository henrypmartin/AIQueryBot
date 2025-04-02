'''
@author: henry Martin
'''
import logging
from com.querybot.utils.db_utils import execute_sql_query, get_database_schema

logger = logging.getLogger(__name__)

# Function to get database schema from MySQL
def get_organization_database_schema():
    
    logger.debug('Getting DB schema for OrganizationDB')
    return get_database_schema('mysql.organization')

def execute_organization_db_sql_query(sql_query):
    
    logger.info("Executing query in OrganizationDB")
    
    return execute_sql_query(sql_query, 'mysql.organization')        
    
if __name__ == "__main__":
    get_database_schema()