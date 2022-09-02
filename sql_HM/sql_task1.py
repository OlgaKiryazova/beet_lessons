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
    connection = create_connection('task_1.sqlite')

    create_job_title_table = """
    CREATE TABLE IF NOT EXISTS job_title (
        id  INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    );
    """

    create_workers_table = """
    CREATE TABLE IF NOT EXISTS workers (
        id  INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT NOT NULL,
        age INTEGER,
        gender VARCHAR(10),
        job_title_id INTEGER NOT NULL, 
        FOREIGN KEY (job_title_id) REFERENCES job_title (id)
    );
    """

    create_department_table = """
    CREATE TABLE IF NOT EXISTS department (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        job_title_id INTEGER NOT NULL, 
        FOREIGN KEY (job_title_id) REFERENCES job_title (id)
    )
    """

    execute_query(connection, create_job_title_table)
    execute_query(connection, create_workers_table)
    execute_query(connection, create_department_table)

    create_job_title = """
    INSERT INTO 
        job_title (name)
    VALUES 
        ('HR manager'),
        ('recruiter'),
        ('sales manager'),
        ('sales'),
        ('lawyer');
    """

    create_workers = """
    INSERT INTO
        workers (full_name, age, gender,job_title_id)
    VALUES 
        ('Ivan Petrov', 30, 'male', 5),
        ('Oleg Fox', 28, 'male', 4),
        ('Sveta Kvitka', 20, 'female', 2),
        ('Victor Chep', 44, 'male', 3),
        ('Nika Tonhf', 40, 'female', 1);
    """

    create_department = """
    INSERT INTO
        department (title, job_title_id )
    VALUES 
        ('Sales department', 3),
        ('Sales department', 4),
        ('HR department', 1),
        ('HR department', 2),
        ('legal department', 5);
    """

    # execute_query(connection, create_job_title)
    # execute_query(connection, create_workers)
    # execute_query(connection, create_department)


    select_departament_workers = """
    SELECT 
        workers.id,
        workers.full_name,
        workers.age,
        department.title
    FROM
        department
    INNER JOIN workers on workers.job_title_id = department.job_title_id
    """

    departament_workers = select_query(connection,  select_departament_workers)

    pprint(departament_workers)

    update_worker = 'UPDATE workers SET age = 35 WHERE full_name = "Victor Chep"'
    delete_worker = 'DELETE FROM workers WHERE full_name = "Nika Tonhf"'

    execute_query(connection, update_worker)
    # execute_query(connection, delete_worker)

    print('#'*80)
    pprint(departament_workers)

    # Почему pprint в строчках 122 и 130 выдают одинаковые данные значений из таблиц,
    #  при этом в строке 127 я меняю данные?
    #

if __name__ == '__main__':
    main()