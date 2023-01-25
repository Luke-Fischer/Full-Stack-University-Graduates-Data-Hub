import psycopg2
from psycopg2 import OperationalError

DATABASE = "psqldb"
USER = "postgres"
PASSWORD = "codegod69"
HOST = "database-1.c4b1rigueer1.us-east-1.rds.amazonaws.com"
PORT = 5432

class SQLClient:
    #Connect to database
    def __init__(self):
        try:
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

    #Create student_info table
    def create_tables(self):
        create_script = '''
                        CREATE TABLE IF NOT EXISTS student_info (
                            student_id INTEGER,
                            student_university VARCHAR(50),
                            student_program VARCHAR(50),
                            student_cumulative_gpa DECIMAL,
                            student_job_found BOOLEAN,
                            student_num_applications INTEGER,
                            student_job_salary INTEGER,
                            student_job_satisfaction INTEGER
                        );'''
        try:
            with self.db.cursor() as curs:
                curs.execute(create_script)
                print("Create Table: SUCCESS")
            self.db.commit()
        except OperationalError as e:
            print("Error in creating tables: "'{e}')

    #Delete student_info table
    def delete_tables(self):
        create_script = '''DROP TABLE IF EXISTS student_info;'''
        try:
            with self.db.cursor() as curs:
                curs.execute(create_script)
                print("Delete Table: SUCCESS")
            self.db.commit()
        except OperationalError as e:
            print("Error in deleting tables: "'{e}')