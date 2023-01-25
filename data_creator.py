import random
from numpy import random


class DataCreator:
    #18 entries
    UNI_LIST = ["Brock University", "Carleton University", "Dalhousie University", "Lakehead University", "McGill University", "McMaster University",
                "Nipissing Univerisity", "Queen's University", "University of British Columbia", "Trent University", "University of Alberta", "University of Calgary",
                "University of Guelph", "Universiy of Manitoba", "University of Toronto", "University of Waterloo", "Wilfrid Laurier University", "York University"]
    
    #28 entries
    PROG_LIST = ["Biology", "Human Nutrition", "Chemical Engineering", "Civil Engineering", "Electrical Engineering", "Mechanical Engineering", "Chemistry", "Physics",
                 "Biomedical Science", "Architecture", "Child Studies", "Gender Studies", "Sociology", "Political Science", "Pyschology", "Computer Science", "Environmental Science",
                 "Finance", "Accounting", "Economics", "Geography", "History", "Human Kinetics", "Computer Engineering", "Studio Art", "Music", "Creative Writing", "Philosophy"]


    def __init__(self, num_entries):
        self.entries = num_entries

    #Generate data for the database
    def populate_database(self):
        university = self.UNI_LIST[(random.randint(0,17))]
        program = self.PROG_LIST[(random.randint(0,27))]

        #Create gpa data
        x_gpa = self.control_overflow(random.normal(loc=2.3, scale=0.8, size=(1)), 0.0, 4.0)
        gpa = float("{:.1f}".format(float(x_gpa)))

        #Create num applications data
        x_num_apps = self.control_overflow(random.normal(loc=250, scale=100, size=(1)), 1.0, 1000.0)
        num_apps = int(x_num_apps)

        #Create salary data
        x_salary = self.control_overflow(random.normal(loc=60000, scale=20000, size=(1)), 5000.0, 500000.0)
        salary = int(x_salary)
        
        #adjust salary to account for GPA
        adjusted_salary = self.compute_adjusted_salary(salary, gpa)

        #Job satisfaction
        job_satisfaction = random.uniform(0.0, 5.0)
        job_satisfaction += (gpa / 10.0)
        adjusted_satisfaction = "{:.1f}".format(self.control_overflow(job_satisfaction, 0.0, 5.0))

        #Example user data entry
        print("University: ", university)
        print("Program: ", program)
        print("GPA: ", gpa)
        print("Number of applications submitted: ", num_apps)
        print("Salary: ", adjusted_salary)
        print("Job Satisfaction: ", adjusted_satisfaction)

        #did they get hired, how long after?


    #Control any possible overflows from the standard deviation
    def control_overflow(self, value, min, max):
        if(value < min):
            return min
        if(value > max):
            return max
        return(value)
    
    def compute_adjusted_salary(self, salary, gpa):
        if(gpa < 1.0):
            salary -= int(salary * (float(gpa) / 60.0))
            return salary
        elif(gpa < 2.0):
            salary -= int(salary * (float(gpa) / 100.0))
            return salary
        elif(gpa < 3.0):
            salary += int(salary * (float(gpa) / 100.0))
            return salary
        else:
            salary += int(salary * (float(gpa) / 60.0))
            return salary
    
