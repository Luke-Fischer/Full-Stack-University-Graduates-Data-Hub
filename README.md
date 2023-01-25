# University-Graduates-Data-Hub
A full-stack web application that holds hypothetical data of Canadian university graduates. The goal of this project is to create a platform where post-grad students can gain a better understanding of how they match up to the current job market.

Tech Stack: HTML5, CSS, Javascript, js frameworks (TBD), Python, PostgreSQL

To connect to database (hosted on AWS): psql --host=database-1.c4b1rigueer1.us-east-1.rds.amazonaws.com --port=5432 --username=postgres --password --dbname=psqldb


# Database set up (subject to changes)
Student ID (INTEGER) 

University Name (VARCHAR)

University Program (VARCHAR)

Cumulative GPA (DECIMAL)

Job Found (TRUE || FALSE)

Num Applications submitted (INTEGER)

Job Salary (DECIMAL)

Job Satisfaction (1-5 (INTEGER))

# Data Set Creation Algorithm Approach 

Number of entries: 10,000

`University Name`: Random

`University Program`: Random

`Cumulative GPA`: Random

`Num Applications`: range (10-500), higher GPA's will submit less applictions

`Job Salary`: range ($30,000 - 120,000) with the majority being somewhere in the middle, higher GPA's are slightly more likely to acquire a higher salary     

`Job Satisfaction`: random
