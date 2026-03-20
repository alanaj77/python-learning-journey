"""
Topic: Conditional Statements
"""

age = int(input("Enter your age: "))

# if statement
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# if-elif-else ladder
marks = int(input("\nEnter your marks: "))

if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 50:
    grade = "C"
else:
    grade = "Fail"

print("Your Grade:", grade)

# Nested if
num = int(input("\nEnter a number: "))

if num >= 0:
    if num == 0:
        print("Number is zero")
    else:
        print("Number is positive")
else:
    print("Number is negative")