# Task 1
import re
from functools import wraps


class Email:

    def __init__(self, email):
        self.validate(email)
        self.email = email

    @classmethod
    def validate(cls, email):
        pattern = '^[^-.#][a-zA-Z\d_\.\?+-]+[^-.#]+@[a-zA-Z0-9-]+.{1}[a-z\-]+[^-.#]+$'
        if re.match(pattern, email):
            return f"{email} is valid"
        else:
            return f"{email} is invalid"


######################################################################################
# Task 2


class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self.workers = []

    def __str__(self):
        return f"{self.__class__.__name__} name: {self.name}, Workers:{self.workers}"

    @property
    def get_workers(self):
        return self.workers

    @get_workers.setter
    def get_workers(self, value):
        self.workers.append(value)


class Worker:
    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        self.boss = boss

    def __str__(self):
        return f"{self.name}"


######################################################################################
# Task 2
class TypeDecorators:

    @staticmethod
    def to_int(func):
        @wraps(func)
        def wrapper(*args):
            return int(func(*args))
        return wrapper

    @staticmethod
    def to_bool(func):
        @wraps(func)
        def wrapper(*args):
            return bool(func(*args))
        return wrapper

    @staticmethod
    def to_float(func):
        @wraps(func)
        def wrapper(*args):
            return float(func(*args))
        return wrapper


@TypeDecorators.to_int
def do_nothing(string: str):
    return string


@TypeDecorators.to_bool
def do_something(string: str):
    return string


@TypeDecorators.to_float
def do_anything(string: str):
    return string


def main():

    print('valid:')
    Email('abc-d@mail.com')
    Email('abc.def@mail.com')
    Email('abc@mail.com')
    Email('abc_def@mail.com')
    Email('abc.def@mail.cc')
    Email('abc.def@mail-archive.com')
    Email('abc.def@mail.org')
    Email('abc.def@mail.com')

    print('invalid:')
    Email('abc-@mail.com')
    Email('abc..def@mail.com')
    Email('.abc@mail.com')
    Email('abc#def@mail.com')
    Email('abc.def@mail.c')
    Email('abc.def@mail#archive.com')
    Email('abc.def@mail')
    Email('abc.def@mail..com')

    boss = Boss(53, "Bob", "Puma")
    print(boss)
    boss.workers = Worker(3453, "Ivan", "Puma", boss)
    print(boss)
    boss.workers = Worker(737, "Max", "Puma", boss)
    print(boss)



    print(do_nothing('25') == 25)
    print(do_something('True') is True)








if __name__ == '__main__':
    main()