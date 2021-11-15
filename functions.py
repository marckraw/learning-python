def something():
    print("Something")


# Function arguments and parameters
def add(x, y):
    result = x + y
    print(result)

add(5, 3)




# Positional arguments
def say_hello(name, surname):
    print(f"Hello {name} and {surname}")

say_hello("Marcin", "Krawczyk")


# Named / Keyword arguments
def say_hello_variable_arguments(name, surname):
    print(f"Hello {name} and {surname}")

say_hello_variable_arguments(name="Marcin", surname="Krawczyk")


# Default argument values
def add_default(x, y=8):
    print(x + y)

add_default(5)
add_default(5, 10)


# Function returning values
def add_and_return(x, y):
    return x + y

result = add_and_return(2, 3)
print(result)


# Lambda functions !!
add_lambda = lambda x, y: x + y
print(add_lambda(5,5))
print( (lambda x, y: x + y)(10,10) )

## Lambda in Map
def double(x):
    return x * 2
sequence = [1,3,5,9]

doubled = [double(x) for x in sequence] # most of the time list comprehension is faster
doubled_list_comprehension_lambda = [(lambda x: x * 2)(x) for x in sequence] # most of the time list comprehension is faster
doubled_map = map(double, sequence)
doubled_lambda = map(lambda x: x * 2, sequence)

print(list(doubled_lambda))

# Unpacking arguments
def multiply(*args):
    print(args)
    total = 1
    for arg in args:
        total = total * arg

    return total

print(multiply(1, 2, 3, 4))


def add_with_arg(x, y):
    return x + y

nums = [3,5]
add_with_arg(*nums) # *nums here = 3, 5

nums_dict = {"x": 15, "y": 25}
add_with_arg(**nums_dict) # becasue nuyms dict has the same keys as what arguments are named in a function


def apply(*args, operator):
    if operator == "*":
        return multiply(*args)
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operation"


print(apply(1, 3, 6, 7, operator="*"))