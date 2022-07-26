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

class AnimalTalks:
    def animal_talk(self, animals):
        for animal in animals:
            animal.talk()


#########################################################
# Task 2

class Author:

    def __init__(self, name_author, country, birthday, books = []):
        self.name_author = name_author
        self.country = country
        self.birthday = birthday
        self.books = books


    # def add_new_author(self, name_author: str,books = [], country = None, birthday= None):
    #     author = {'name_author': name_author,
    #               'country': country,
    #               'birthday': birthday,
    #               'books': books
    #               }
    #     self.authors.append(author)

    def __repr__(self):
        return f' Author {self.name_author} {self.country} {self.birthday}'

    def __str__(self):
        return f'Author {self.name_author} {self.country} {self.birthday}'


class Book:
    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author

    # def add_book(self, name, year, author):
    #     self.books.append(name, year, author)
    #
    # def __repr__(self):
    #     return f'book {self.name} {self.year}'
    #
    # def __str__(self):
    #     return f'book{self.name} {self.year}'

    def __str__(self):
        return '"{}" by {}'.format(self.name, self.author)

    def __repr__(self):
        return str(self)



class Library:
    # def __init__(self, name, books = [], authors = []):
    #     self.name = name
    #     self.books = books
    #     self.authors = authors

    def __init__(self):
        self.books = []
        self.authors = []

    def new_book(self, name: str, year: int, author):
        # add_book(name, year, author)
        book = {'name': name, 'year': year, 'author': author}
        self.books.append(book)
        if author not in self.authors:
            self.authors.append(author)
            # name_author = author
            # books = self.books
            # country = None
            # birthday = None
            # author.add_new_author(name_author,  books,  country = None, birthday = None,)
        print(f'{name} added')

    def group_by_author(self, author):
        for book in self.books:
            if book.get('author') == author:
                print(book)
        else:
            print('author not found')

    def group_by_year(self, year: int):
        for book in self.books:
            if book.get('year') == year:
                print(book)
            else:
                print('year not found')


    def __repr__(self):
        return f'{self.__class__.__name__} library'

    def __str__(self):
        return f'{self.__class__.__name__} library'



#########################################################################
# Task 3
class Fraction:
    pass

def main():
    animals = [Cat('Lulu'), Dog('Rex'), Cat('Sonya')]
    talks = AnimalTalks()
    talks.animal_talk(animals)
    book1 = Book('1984', 1949,'George Orwel')
    book2 = Book('Animal Farm', 1945, 'George Orwel')
    book3 = Book('Fahrenheit 451', 1953, 'Raymond Bradbury')
    l = Library()
    l.new_book('1984', 1949, 'George Orwel')
    l.new_book('Animal Farm', 1945, 'George Orwel')
    l.new_book('Fahrenheit 451', 1953, 'Raymond Bradbury')
    print(l.books)
    l.group_by_author('George Orwel')
    l.group_by_year(1945)






if __name__ == '__main__':
    main()