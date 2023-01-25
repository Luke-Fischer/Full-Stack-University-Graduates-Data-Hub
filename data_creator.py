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

        #Create gpa resembling a standard deviation
        x = self.control_overflow(random.normal(loc=2.3, scale=0.8, size=(1)))
        gpa = "{:.1f}".format(x[0])

    #Control any possible overflows from the standard deviation
    def control_overflow(slef, gpa):
        if(gpa[0] < 0.0):
            return 0.0
        if(gpa[0] > 4.0):
            return 4.0
        return(gpa)
