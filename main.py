from sql_client import SQLClient
from data_creator import DataCreator

#Test connection to database - PASSED 
data = DataCreator(10)
data.populate_database()