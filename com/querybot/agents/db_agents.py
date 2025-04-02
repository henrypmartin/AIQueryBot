'''
@author: Henry Martin
'''

import logging
from com.querybot.agents import mysql_organization_db, mysql_college_db

logger = logging.getLogger(__name__)

def mysql_organization_db_scheme_generation_agent(user_query: str) -> str:
    ''' Tool to generate the schema for organization database from mysql instance.
    '''
    
    schema = mysql_organization_db.get_organization_database_schema()
    
    logger.info(f'mysql organization db schema: {schema}')
    
    return schema

def mysql_organization_db_query_execution_agent(sql_query: str) -> str:
    ''' Agent to execute the query for organization database from mysql instance and return the results of the query execution.
    '''
    
    data = mysql_organization_db.execute_organization_db_sql_query(sql_query)
    
    print(f'Query execution results {data}')
    
    return data

def mysql_college_db_scheme_generation_agent(user_query: str) -> str:
    ''' Tool to generate the schema for college database from mysql instance.
    '''
    
    schema = mysql_college_db.get_college_database_schema()
    
    logger.info(f'mysql college db schema: {schema}')
    
    return schema

def mysql_college_db_query_execution_agent(sql_query: str) -> str:
    ''' Agent to execute the query for college database from mysql instance and return the results of the query execution.
    '''
    
    data = mysql_college_db.execute_college_db_sql_query(sql_query)
    
    print(f'Query execution results {data}')
    
    return data
