"""
Topic: Functions in Python
"""

# Simple function
def greet():
    print("Hello, welcome to Python!")

greet()

# Function with parameters
def greet_user(name):
    print(f"Hello, {name}!")

greet_user("Alan")

# Function with return value
def add(a, b):
    return a + b

result = add(10, 5)
print("Sum:", result)

# Default parameters
def power(base, exponent=2):
    return base ** exponent

print("Square:", power(4))
print("Cube:", power(4, 3))

# Keyword arguments
def student_info(name, age):
    print(f"Name: {name}, Age: {age}")

student_info(age=20, name="Alan")

# Variable-length arguments
def total_sum(*numbers):
    return sum(numbers)

print("Total:", total_sum(1, 2, 3, 4, 5))

# Lambda function
square = lambda x: x * x
print("Square using lambda:", square(6))