"""
Topic: Loops in Python
"""

# For loop
print("For Loop Example:")
for i in range(1, 6):
    print("Number:", i)

# While loop
print("\nWhile Loop Example:")
count = 1
while count <= 5:
    print("Count:", count)
    count += 1

# Loop control statements
print("\nBreak Example:")
for i in range(1, 10):
    if i == 5:
        break
    print(i)

print("\nContinue Example:")
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

# Loop with else
print("\nLoop with Else:")
for i in range(3):
    print(i)
else:
    print("Loop finished successfully")