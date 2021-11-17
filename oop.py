class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades)


student = Student("Bob", (90, 90, 93, 78, 20))
student2 = Student("Rolf", (1, 2, 93, 34, 120))

print(student.name)
print(student.grades)
print(student.average_grade())

print()

print(student2.name)
print(student2.grades)
print(student2.average_grade())

########################################
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self): # kind of like toString()
        return f"Person {self.name}, {self.age}"

    def __repr__(self): # unabigouse representation of an object for recreating this object
        return f"<Person({self.name}, {self.age})>"

bob = Person("Bob", 35)
print(bob)

########################################
class ClassTest:
    def instance_method(self): # all the methods related to instances of a class
        print(f"Called instance_method of {self}")

    @classmethod
    def class_method(cls): # often used as factories
        print(f"called class_method of {cls}")

    @staticmethod
    def static_method(): # just function inside a class - doesnt have any information about class or about object
        print("Called static method")



test = ClassTest()
print(test.instance_method())

ClassTest.class_method()
ClassTest.static_method()

print()
print()
print()

########################################
class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}g>"

    @classmethod
    def hardcover(cls, name, page_weight):
        return cls(name, cls.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name, page_weight):
        return cls(name, cls.TYPES[1], page_weight)

book = Book.hardcover("Harry Potter", 1500)
book2 = Book.paperback("Comic Book", 600)
print(book)
print(book2)

print()
print()
print()

#################### inheritance ##########################
class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True

    def __str__(self):
        return f"Device {self.name!r} ({self.connected_by})"

    def disconnect(self):
        self.connected = False
        print("Disconnected.")

class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        super().__init__(name, connected_by)
        self.capacity = capacity
        self.remaining_pages = capacity

    def __str__(self):
        return f"{super().__str__()} ({self.remaining_pages} pages remaining)"

    def print(self, pages):
        if not self.connected:
            print("Printer not connected")
        print(f"Printing {pages}")
        self.remaining_pages -= pages

printer = Printer("Printer", "USB", 500)
printer.print(200)
printer.print(50)
print(printer)
printer.disconnect()

print()
print()
print()
############### Class Composition ######################
class BookShelf:
    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f"BookShelf with {len(self.books)} books."

class Book:
    def __init__(self, name):
        self.name = name

book = Book("Harry Potter")
book2 = Book("Python 101")
book3 = Book("Another book")

shelf = BookShelf(book, book2, book3)
print(shelf)