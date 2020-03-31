# default parameters, keyword arguments
def add(a=10, b=20):
    return a+b


add()  # 30
add(1, 10)  # 11


def add(a, b):
    return a+b


def math(a, b, fn=add):
    return fn(a, b)


def subtract(a, b):
    return a-b


math(2, 2)  # 4

math(2, 2, subtract)  # 0

# scope - global
total = 0


def increment():
    global total
    total += 1
    return total


increment()  # 1

# scope - nonlocal


def outer():
    count = 0

    def inner():
        nonlocal count
        count += 1
        return count
    return inner()

# documenting fuctions


def say_hello():
    """A simple function that returns the string hello"""
    return "Hello!"


say_hello.__doc__  # 'A simple function that returns the string hello'

# *args - Gathers remaining keyword arguments as a tuple


def sum_all_values(*args):
    total = 0
    for val in args:
        total += val

    return total


sum_all_values(1, 2, 3)  # 6

sum_all_values(1, 2, 3, 4, 5)  # 15

# **kwargs - Gathers remaining keyword arguments as a dictionary


def favorite_colors(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}'s favorite color is {value}")


favorite_colors(rusty='green', colt='blue')


def display_info(a, b, *args, instructor="Sun", **kwargs):
    return [a, b, args, instructor, kwargs]


display_info(1, 2, 3, last_name="Lee", job="Developer")

[1, 2, (3,), 'Sun', {'job': 'Developer', 'last_name': 'Lee'}]

# using * as an Argument - Argument Unpacking


def sum_all_values(*args):
    # there's a built in sum function - we'll see more later!
    return sum(args)


sum_all_values([1, 2, 3, 4])  # nope...
sum_all_values((1, 2, 3, 4))  # this does not work either...

sum_all_values(*[1, 2, 3, 4])  # 10
sum_all_values(*(1, 2, 3, 4))  # 10

# using ** as an Argument - Dictionary Unpacking


def display_names(first, second):
    return f"{first} says hello to {second}"


names = {"first": "Sun", "second": "Tom"}

display_names(names)  # nope..

display_names(**names) "Sun says hello to Tom"

# Lambdas - anonymous functions


def first_lambda(x): return x + 5

first_lambda(10)  # 15

first_lambda.__name__  # '<lambda>'


def add_values(x, y): return x + y


def multiply_values(x, y): return x + y


add_values(10, 20)  # 30

multiply_values(10, 20)  # 200
