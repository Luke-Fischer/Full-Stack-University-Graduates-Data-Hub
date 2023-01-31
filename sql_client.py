import psycopg2
from psycopg2 import OperationalError
from data_creator import DataCreator

DATABASE = "psqldb"
USER = "postgres"
PASSWORD = "psql_pass"
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
                            student_job_satisfaction DECIMAL,
                            student_months_since_grad INTEGER
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

    #fill tables
    def fill_tables(self):
        data_creator = DataCreator()
        for i in range (10000):
            fill_script = data_creator.populate_database(i)
            try:
                with self.db.cursor() as curs:
                    curs.execute(fill_script)
                self.db.commit()
            except OperationalError as e:
                print("Error in filling tables: "'{e}')
        print("Filling Table: SUCCESS")

    # Creating a generic query that will return an ordered list of elemets depending on user input - where param is (gpa, num_apps, rate of hired,...etc.)
    def hired_avg_university(self):
        #return universities with hiring rate
        for university in DataCreator.UNI_LIST:
            select_script = "SELECT COUNT(*) FROM student_info where student_job_found = 't' AND student_university = '" + university + "';"
            total_students_script = "SELECT COUNT(*) FROM student_info where student_university = '" + university + "';"
            try:
                with self.db.cursor() as curs:
                    #Num hired grads
                    curs.execute(select_script)
                    output = curs.fetchall()
                    nominator = float(output[0][0])

                    #Num grads
                    curs.execute(total_students_script)
                    output = curs.fetchall()
                    denominator = float(output[0][0])

                    result = "{:.1f}".format(float((nominator / denominator) * 100.0))
                    print(university, result)

            except OperationalError as e:
                print("Error in query: "'{e}')

    def computable_avg_university(self, param):
        index = 0
        if(param == "gpa"):
            index = 3
        elif(param == "num_apps"):
            index = 5
        elif(param == "salary"):
            index = 6
        elif(param == "satisfaction"):
            index = 7
        else:
            print("Error - invalid query type")

        for university in DataCreator.UNI_LIST:
            count = 0.0
            result = 0.0
            select_script = "SELECT * FROM student_info where student_university = '" + university + "';"
            try:
                with self.db.cursor() as curs:
                    curs.execute(select_script)
                    output = curs.fetchall()
                    for row in output:
                        if(row[4] == True):
                            result += float(row[index])
                            count += 1.0
                    result = "{:.2f}".format(result / count)
                    print(university, result)
            except OperationalError as e:
                print("Error in query: "'{e}')

    #query to return a schools most common major
    def most_common_major(self):
        for university in DataCreator.UNI_LIST:
            max = 0
            max_prog = ""
            for program in DataCreator.PROG_LIST:
                select_script = "SELECT COUNT(*) FROM student_info where student_university = '" + university+ "' and student_program = '" + program + "';"
                try:
                    with self.db.cursor() as curs:
                        curs.execute(select_script)
                        output = curs.fetchall()
                        temp = int(output[0][0])
                        if (temp > max):
                            max = temp
                            max_prog = program
                except OperationalError as e:
                    print("Error in query: "'{e}')
            print(university, max_prog)


