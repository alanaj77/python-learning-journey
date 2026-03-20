"""
Topic: Variables and Data Types in Python
"""

# Variables
name = "Alan"
age = 20
height = 1.75
is_student = True

# Printing variables
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is Student:", is_student)

# Data Types
print("\n--- Data Types ---")
print(type(name))        # str
print(type(age))         # int
print(type(height))      # float
print(type(is_student))  # bool

# Multiple assignment
x, y, z = 10, 20, 30
print("\nMultiple Assignment:", x, y, z)

# Type casting
num_str = "100"
num_int = int(num_str)
print("\nConverted Integer:", num_int, type(num_int))