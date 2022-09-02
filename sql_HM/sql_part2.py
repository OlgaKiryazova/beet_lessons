from pprint import pprint

from sql_task2 import create_connection, select_query

connection = create_connection('hr.db')


# 1. write a query in SQL to display the first name, last name,
# department number, and department name for each employee
select_data_employee = """
SELECT E.first_name || ' ' || E.last_name, E.department_id, D.department_name   
FROM employees AS E
JOIN department AS D ON E.department_id =  D.department_id
"""
# result = select_query(connection, select_data_employee)
# pprint(result)


# 2 write a query in SQL to display the first and last name, department,
# city, and state province for each employee
select = """
SELECT 
    E.first_name || ' ' || E.last_name, 
    D.department_name, 
    l.city, 
    L.state_province   
FROM employees AS E
JOIN department AS D ON E.department_id =  D.department_id
JOIN locations AS L ON L.location_id  = D.location_id

"""
# result = select_query(connection, select)
# pprint(result)


# 3 write a query in SQL to display the first name, last name, department
# number, and department name, for all employees for departments 80 or 40
select = """
SELECT 
    E.first_name || ' ' || E.last_name,
    D.department_id,
    D.department_name   
FROM employees AS E
JOIN department AS D ON E.department_id =  D.department_id
where D.department_id in (80, 40)

"""
# result = select_query(connection, select)
# pprint(result)


# 4 write a query in SQL to display all departments including those where
# does not have any employee
select = """SELECT * FROM  departments """
# result = select_query(connection, select)
# pprint(result)


# 5. write a query in SQL to display the first name of all employees
# including the first name of their manager
select_first_name = """
SELECT employees.first_name, manager.first_name
FROM employees 
join employees AS manager 
 ON employees.manager_id = manager.employee_id
"""
# first_name_employees = select_query(connection, select_first_name)
# pprint(first_name_employees)


# 6. write a query in SQL to display the job title, full name
# (first and last name ) of the employee, and the difference between
# the maximum salary for the job and the salary of the employee
select = """
SELECT 
    J.job_title,
    E.first_name || ' ' || E.last_name,
    (J.max_salary - E.salary)
FROM employees AS E
JOIN jobs AS J ON J.job_id =  E.job_id


"""
result = select_query(connection, select)
pprint(result)


# 7 write a query in SQL to display the job title and the average salary of employees
select = """
SELECT 
    job_title,
    (max_salary + min_salary)/2
FROM jobs 
"""
# result = select_query(connection, select)
# pprint(result)


#8 write a query in SQL to display the full name (first and last name), and
# salary of those employees who work in any department located in London
select = """
SELECT 
    E.first_name || ' ' || E.last_name, 
    E.salary,
    L.city  
FROM employees AS E
JOIN department AS D ON E.department_id =  D.department_id
JOIN locations AS L ON L.location_id  = D.location_id 
where L.City = 'London' 

"""
result = select_query(connection, select)
pprint(result)


#9 write a query in SQL to display the department name and the number of
#employees in each department
select = """
SELECT D.depart_name, COUNT(e.employee_id)
FROM departments as D
JOIN employees as E ON E.department_id = D.department_id
GROUP BY D.depart_name
"""
# result = select_query(connection, select)
# pprint(result)