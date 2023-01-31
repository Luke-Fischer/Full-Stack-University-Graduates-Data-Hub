import random
from numpy import random


class DataCreator:
    #17 entries
    UNI_LIST = ["Brock University", "Carleton University", "Dalhousie University", "Lakehead University", "McGill University", "McMaster University",
                "Nipissing Univerisity", "Queens University", "University of British Columbia", "Trent University", "University of Alberta", "University of Calgary",
                "University of Guelph", "Universiy of Manitoba", "University of Toronto", "University of Waterloo", "Wilfrid Laurier University"]
    
    #28 entries
    PROG_LIST = ["Biology", "Human Nutrition", "Chemical Engineering", "Civil Engineering", "Electrical Engineering", "Mechanical Engineering", "Chemistry", "Physics",
                 "Biomedical Science", "Architecture", "Child Studies", "Gender Studies", "Sociology", "Political Science", "Pyschology", "Computer Science", "Environmental Science",
                 "Finance", "Accounting", "Economics", "Geography", "History", "Human Kinetics", "Computer Engineering", "Studio Art", "Music", "Creative Writing", "Philosophy"]

    #Generate data for the database
    def populate_database(self, id):
        hired = False

        university = self.UNI_LIST[(random.randint(0,17))]
        program = self.PROG_LIST[(random.randint(0,27))]

        #Create gpa data
        x_gpa = self.control_overflow(random.normal(loc=2.3, scale=0.8, size=(1)), 0.0, 4.0)
        gpa = float("{:.1f}".format(float(x_gpa)))

        #Create salary data
        x_salary = self.control_overflow(random.normal(loc=60000, scale=10000, size=(1)), 5000.0, 500000.0)
        salary = int(x_salary)
        
        #adjust salary to account for GPA
        adjusted_salary = self.compute_adjusted_salary(salary, gpa)

        #Job satisfaction
        job_satisfaction = random.uniform(0.0, 5.0)
        job_satisfaction += (gpa / 10.0)
        adjusted_satisfaction = "{:.1f}".format(self.control_overflow(job_satisfaction, 0.0, 5.0))

        #months after graduated
        x_months_since_grad = self.control_overflow(random.normal(loc=5, scale=3, size=(1)), 0.0, 100.0)
        months_since_grad = int(x_months_since_grad)

        #Create num applications data
        x_num_apps = self.control_overflow(random.normal(loc=250, scale=100, size=(1)), 1.0, 1000.0)
        num_apps = int(x_num_apps)

        #adjust for time after graduation consideration
        num_apps += (months_since_grad * 10) 

        #Has found job (y/n) - number of applications + gpa will have an affect on this parameter - determined by (num_applications submitted / 10 + (gpa * 10))
        percentage = self.control_overflow(float(float(num_apps) / 10.0) + (float(gpa) * 10.0) + 10.0, 0.0, 100.0)
        rand = random.uniform(0.0, 100.0)

        if(rand <= percentage):
            hired = True
        
        if(hired == False):
            adjusted_salary = 0
            adjusted_satisfaction = 0

        #send data to filling algo - explicitly casting
        fill_script = '''INSERT INTO student_info(student_id, student_university, student_program, student_cumulative_gpa, student_job_found, student_num_applications, 
                         student_job_salary, student_job_satisfaction, student_months_since_grad) VALUES ({0}, \'{1}\', \'{2}\', {3}, {4}, {5}, {6}, {7}, {8});'''
        
        return fill_script.format(id, university, program, gpa, hired, num_apps, adjusted_salary, adjusted_satisfaction, months_since_grad)

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
    
