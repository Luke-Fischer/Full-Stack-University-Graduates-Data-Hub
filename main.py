from sql_client import SQLClient

#Test connection to database - PASSED 
sql_client = SQLClient()
sql_client.delete_tables()
sql_client.create_tables()
sql_client.fill_tables()
