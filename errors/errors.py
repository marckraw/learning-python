def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Divisor cannot be 0.") # exception object

    return a / b


# grades = [78, 99, 86, 100]
grades = []

try:
    average = divide(sum(grades), len(grades))
except ZeroDivisionError as e:
    print("There are no grades yet in your list.")
except ValueError:
    print("Some different error")
else:
    print("Succeed")
    print(average)
finally:
    print("Run always")

############################################################ Custom error classes

class TooManyPagesReadError(ValueError):
    pass

class Book:
    def __init__(self, name: str, page_count: int):
        self.name = name
        self.page_count = page_count
        self.pages_read = 0

    def __repr__(self):
        return (
            f"<Book {self.name}, read {self.pages_read} pages out of {self.page_count}>"
        )

    def read(self, pages):
        if self.pages_read + pages > self.page_count:
            raise TooManyPagesReadError("To many pages read mate")

        self.pages_read += pages
        print("You have read some", self.pages_read, "out off", self.page_count)



book = Book("Harry potter", 50)

try:
    book.read(50)
    book.read(150)
except TooManyPagesReadError:
    print("meh")