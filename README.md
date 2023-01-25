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

`Cumulative GPA`: Random with a normal distribution using the mean of 2.3 and standard deviation of 0.8.

`Num Applications`: Random with a normal distribution using the mean of 250 and standard deviation of 100.

`Job Salary`: Random with a normal distribution using the mean of 65,000 and standard deviation of 30,000. GPA will have an effect on this parameter.

`Job Satisfaction`: random. GPA will have an affect on this parameter.
