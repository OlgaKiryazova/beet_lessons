class Person:
    def __init__(self, name, age, status):
        self.name = name
        self.age = age
        self.status = status

    def __str__(self):
        return self.name + ' ' + self.status


class Student(Person):
    def __init__(self, name, age, status):
        super().__init__(name, age, status)
        self.rating = {}
        self.knowledge = []

    def studied_topic(self, topic):
        self.knowledge.append(topic)

    def get_rated(self, topic, score):
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

    def rate(self, student, topic, score):
        student.get_rated(topic, score)
        print(f'{student.name} has been rated of {score} points')

    def lessons(self):
        print(f'Finished {self.count_lesson} lessons')

    def calculate_payroll(self):
        print(f'{self.salary} salary')


##################################################################################
# Task 2

class Mathematician:

    def square_nums(self, list):
        print([num ** 2 for num in list])

    def remove_positives(self, list):
        print([num for num in list if num < 0])

    def filter_leaps(self, list):
        print([year for year in list if year % 4 == 0])


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
    def __init__(self, product: Product):
        self.product = product

    def add(self, amount):
        self.amount += amount
        self.price = self.price * 1.3
        print(f'{self.name} {amount}  added')

    # def set_discount(self, percent, identifier_type = 'name'):
    #     self.price = self.price * (100-percent)
    #     print(self.product.name, self.price)


    # def sell_product(self, product_name, amount):
    #     if product_name in Product.data:
    #
    #         self.amount = self.amount-amount
    #     print(self)












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
    s = ProductStore
    s.add(p, 10)
    s.add(p, 10)
    s.add(p2, 300)
    # s.sell_product('Ramen', 10)
    print(p)



if __name__ == '__main__':
    main()