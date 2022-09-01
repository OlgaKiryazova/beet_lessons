from pprint import pprint

import sqlite3
from sqlite3 import Error


def create_connection(path: str):
    connection = None
    try:
        connection = sqlite3.connect(path)
    except Error as e:
        print(f'Sqlite connectio error {e}')

    return connection


def execute_query(connection, query: str):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
    except Error as e:
        print(f'Sqlite connectio error {e}')


def select_query(connection, query: str):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f'Sqlite connection error {e}')


def main():
    connection = create_connection('hr.db')

# write a query to display the names (first_name, last_name) using alias name
# "First Name", "Last Name" from the table of employees;

    select_employees = """
    SELECT 
        first_name as [First Name], 
        last_name as [Last Name] 
     FROM employees
    """

    full_name_employees = select_query(connection,  select_employees)
    pprint(full_name_employees)

#write a query to get the unique department ID from the employee table
    select_department_id = "SELECT DISTINCT department_id FROM employees"
    unique_dep_id_query = select_query(connection, select_department_id)
    pprint(unique_dep_id_query)


#write a query to get all employee details from the employee table ordered
# by first name, descending
    select_all_details_query = "SELECT * FROM employees ORDER BY first_name DESC"
    get_all_details_query = select_query(connection, select_all_details_query)
    print(get_all_details_query)

# write a query to get the names (first_name, last_name), salary,
    # PF of all the employees (PF is calculated as 12% of salary)
    select_pf_query = """
    SELECT 
        first_name, 
        last_name, 
        salary, 
        (salary*0.12)
    FROM employees
        """
    pf_query = select_query(connection, select_pf_query)
    pprint(pf_query)

#write a query to get the maximum and minimum salary from the employees table
    select_min_max_salary = "SELECT MIN(salary), MAX(salary) FROM employees"
    min_max_salary = select_query(connection, select_min_max_salary)
    pprint(min_max_salary)

#write a query to get a monthly salary (round 2 decimal places) of each
    # and every employee
    select_round_salary = """
    SELECT 
        first_name, 
        last_name, 
        ROUND(salary-salary*0.12, 2)
    FROM employees 
    """
    round_salary = select_query(connection, select_round_salary)
    pprint(round_salary)



if __name__ == '__main__':
    main()