import psycopg2

DATABASE = "psqldb"
USER = "postgres"
PASSWORD = "codegod69"
HOST = "database-1.c4b1rigueer1.us-east-1.rds.amazonaws.com"
PORT = 5432

class SQLClient:
    def __init__(self):
        try:
            #Connect to database
            self.db = psycopg2.connect(
                database = DATABASE,
                user = USER,
                password = PASSWORD,
                host = HOST,
                port = PORT,
            )
            print("Connection to PostgreSQL DB successful")
        except:
            print("Error occurred in connecting to the DB")
