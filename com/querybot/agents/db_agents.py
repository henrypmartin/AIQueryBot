'''
@author: Henry Martin
'''

import logging
from com.querybot.agents import mysql_organization_db

logger = logging.getLogger(__name__)

def mysql_organization_db_scheme_generation_agent(user_query: str) -> str:
    ''' Tool to generate the schema for organization database from mysql instance.
    '''
    
    schema = mysql_organization_db.get_database_schema()
    
    schema_temp = '''
            Table: Departments
            Columns: DepartmentID, DepartmentName, Location
            
            Table: Employees
            Columns: EmployeeID, FirstName, LastName, Email, Phone, HireDate, DepartmentID, RoleID
            
            Table: Roles
            Columns: RoleID, RoleName, Salary
            
            Table: Projects
            Columns: ProjectID, ProjectName, StartDate, EndDate, Budget
            
            Table: Employee_Project
            Columns: ProjectID, EmployeeID, AssignmentDate
            '''
    
    logger.info(f'mysql organization db schema: {schema}')
    
    return schema

def mysql_organization_db_query_execution_agent(sql_query: str) -> str:
    ''' Agent to execute the query for organization database from mysql instance and return the results of the query execution.
    '''
    
    data = mysql_organization_db.execute_sql_query(sql_query)
    
    print(f'Query execution results {data}')
    
    return data

def mysql_college_db_scheme_generation_agent(user_query: str) -> str:
    ''' Tool to generate the schema for college database from mysql instance.
    '''
    
    #schema = mysql_organization_db.get_database_schema()
    
    schema = '''
            Table: Departments
            Columns: DepartmentID, DepartmentName, Location
            
            Table: Students
            Columns: StudentID, FirstName, LastName, Email, Phone, EnrollmentDate
            
            Table: Courses
            Columns: CourseID, Name, DepartmentID
            
            Table: Enrollments
            Columns: EnrollmentID, StudentID, CourseID, Grade
            '''
    
    logger.info(f'mysql college db schema: {schema}')
    
    return schema

def mysql_college_db_query_execution_agent(sql_query: str) -> str:
    ''' Agent to execute the query for college database from mysql instance and return the results of the query execution.
    '''
    
    #data = mysql_organization_db.execute_sql_query()
    
    data = "dummy data from college sql query execution"
    print(f'Query execution results {data}')
    
    return data
