CREATE TABLE IF NOT EXISTS student_info (
	student_id INTEGER,
    student_university VARCHAR(50),
    student_program VARCHAR(50),
    student_cumulative_gpa DECIMAL,
    student_job_found BOOLEAN,
    student_num_applications INTEGER,
    student_job_salary INTEGER,
    student_job_satisfaction INTEGER
);

-- possible for a university table in the future to simulate university info (i.e application acceptance, num applications, etc...)
