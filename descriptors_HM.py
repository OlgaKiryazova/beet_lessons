# Task 1
import re


class Email:

    def __init__(self, email):
        self.validate(email)
        self.email = email

    @classmethod
    def validate(cls, email):
        pattern = '^[^-.#][a-zA-Z\d_\.\?+-]+[^-.#]+@[a-zA-Z0-9-]+.{1}[a-z\-]+[^-.#]+$'
        if re.match(pattern, email):
            print(f"{email} is valid")
        else:
            print(f"{email} is invalid")


######################################################################################
# Task 2


class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self.workers = []

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
        # boss.get_workers(name)

    @property
    def get_boss(self):
        return self.boss

    @get_boss.setter
    def get_boss(self, value):
        self.boss = value


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
    worker1 = Worker(3453, "Ivan", "Puma", boss)
    worker2 = Worker(737, "Max", "Puma", boss)
    print(boss.workers)
    print(boss.get_workers)
    print(boss.workers)
    # print(boss.get_workers(worker1))
    # print(boss.workers)
    # print(boss.get_workers(worker2))
    # print(boss.workers)







if __name__ == '__main__':
    main()