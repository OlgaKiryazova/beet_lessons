class Person:
    def __init__(self, name, age, status):
        self.name = name
        self.age = age
        self.status = status

    def __str__(self):
        return f'{self.name}  {self.status}'


class Student(Person):
    def __init__(self, name, age, status):
        super().__init__(name, age, status)
        self.rating = {}
        self.knowledge = []

    def studied_topic(self, topic):
        self.knowledge.append(topic)

    def set_rated(self, topic, score):
        self.rating.update({topic: score})

    def learned_topics(self):
        print(f'{self} learned such topics- {self.knowledge}')


class Teacher(Person):
    def __init__(self, name, age, status, salary):
        super().__init__(name, age, status)
        self.salary = salary
        self.count_lesson = 0

    def teach(self, topic, *student):
        for i in student:
            i.studied_topic(topic)
        self.count_lesson += 1
        print(f'lesson {topic} completed')

    @staticmethod
    def rate(student, topic, score):
        student.set_rated(topic, score)
        print(f'{student.name} has been rated of {score} points')

    def lessons(self):
        print(f'Finished {self.count_lesson} lessons')

    def calculate_payroll(self):
        print(f'{self.salary} salary')


##################################################################################
# Task 2

class Mathematician:

    @staticmethod
    def square_nums(list_):
        print([num ** 2 for num in list_])

    @staticmethod
    def remove_positives(list_):
        print([num for num in list_ if num < 0])

    @staticmethod
    def filter_leaps(list_):
        print([year for year in list_ if year % 4 == 0])


########################################################################################
# Task 3


class Product:

    def __init__(self, type_product, name, price):
        self.type_product = type_product
        self.name = name
        self.price = price
        self.amount = 0

    def __str__(self):
        return f'{self.name} in stock {self.amount}'


class ProductStore:
    def __init__(self):
        self.products = []
        self.income = 0

    def add(self, product, amount):
        self.products.append(product)
        product.price = round(product.price * 1.3, 2)
        product.amount += amount
        print(f'{product.name} {amount} units added')

    def set_discount(self, identifier, percent, identifier_type = 'name'):
        if identifier_type == 'name':
            for product in self.products:
                if product.name == identifier:
                    product.price *= (1 - percent/100)
        elif identifier_type == 'type':
            for product in self.products:
                if product.type_product == identifier:
                    product.price *= (1 - percent/100)

    def sell_product(self, product_name, amount):
        for product in self.products:
            if product.name == product_name and product.amount >= amount:
                product.amount -= amount
                self.income += product.price * amount
                print(f'{product.name} sell {amount} units')

    def get_income(self):
        return self.income

    def get_all_products(self):
        for product in self.products:
            print(f'{product.name}, price: {product.price}, amount :{product.amount}')

    def get_product_info(self, product_name):
        for product in self.products:
            if product.name == product_name:
                print(product.__dict__)
        else:
            print(f'{product_name} is not in the list')

################################################################################
# Task 4


class CustomException(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        with open('logs.txt', 'a') as f:
            f.write(msg + '\n')


def main():
    # Task 1
    student1 = Student('Ivan', 18, 'student')
    student2 = Student('Max', 18, 'student')
    teacher1 = Teacher('Oleg Petrovich ', 40, 'teacher', 2000)

    teacher1.teach('topic1', student1, student2)
    teacher1.teach('topic2', student1, student2)
    teacher1.teach('topic3', student1)

    teacher1.lessons()
    print(student1)
    print(student1.knowledge)
    student1.learned_topics()

    teacher1.rate(student1, 'topic 1', 5 )
    print(student1.rating)
    teacher1.rate(student1, 'topic 2', 3)
    print(student1.rating)
    teacher1.calculate_payroll()

    print('#' * 80)

    # Task 2
    m = Mathematician()
    m.square_nums([7, 11, 5, 4])
    m.remove_positives([26, -11, -8, 13, -90])
    m.filter_leaps([2001, 1884, 1995, 2003, 2020])
    print('#' * 80)

    p = Product('Sport', 'Football T-Shirt', 100)
    p2 = Product('Food', 'Ramen', 1.5)
    s = ProductStore()
    s.add(p, 10)
    s.add(p, 10)
    s.add(p2, 300)
    s.sell_product('Ramen', 10)
    print(p)
    print(p2)
    s.get_product_info('Ramen')
    s.get_product_info('fdh')
    print(s.income)
    s.get_all_products()






if __name__ == '__main__':
    main()