# Task 1

class Animal:
    def __init__(self, name):
        self.name = name

    def talk(self):
        raise NotImplementedError('must be implemented by a sub class')


class Cat(Animal):
    def talk(self):
        print(f'{self.name} Meow')


class Dog(Animal):
    def talk(self):
        print(f'{self.name} Woof-woof')


def animal_talk(animals):
    for animal in animals:
        animal.talk()


#########################################################
# Task 2

class Author:

    def __init__(self, name, country, birthday, books = []):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = books

    def __repr__(self):
        return f' Author {self.name} {self.country} {self.birthday}'

    def __str__(self):
        return f'Author {self.name} {self.country} {self.birthday}'


class Book:
    def __init__(self, name, year, author: Author):
        self.name = name
        self.year = year
        self.author = author

    def __str__(self):
        return f'{self.name} by {self.author}'

    def __repr__(self):
        return f'{self.name} by {self.author}'


class Library:

    def __init__(self):
        self.books = []
        self.authors = []

    def new_book(self, name: str, year: int, author: Author):
        book = Book(name, year, author)
        self.books.append(book)
        if author not in self.authors:
            self.authors.append(author)
        print(f'Book "{name}" added')

    def group_by_author(self, author):
        for book in self.books:
            if book.author == author:
                print(book)

    def group_by_year(self, year: int):
        for book in self.books:
            if book.year == year:
                print(book)

    def __repr__(self):
        return f'{self.__class__.__name__}'

    def __str__(self):
        return f'{self.__class__.__name__}'



#########################################################################
# Task 3





def main():
    animals = [Cat('Lulu'), Dog('Rex'), Cat('Sonya')]
    animal_talk(animals)

    l = Library()
    l.new_book('1984', 1949, 'George Orwel')
    l.new_book('Animal Farm', 1945, 'George Orwel')
    l.new_book('Fahrenheit 451', 1953, 'Raymond Bradbury')
    print(l.books)
    l.group_by_author('George Orwel')
    l.group_by_year(1945)





if __name__ == '__main__':
    main()