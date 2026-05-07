import os

filename = input("Enter file name: ")

if not os.path.exists(filename):
    print("Error: File does not exist.")
    exit()

if os.path.getsize(filename) == 0:
    print("Error: File is empty.")
    exit()

try:
    marks = input("Enter marks: ")

    if marks.strip() == "":
        raise ValueError("Marks cannot be empty.")

    marks = float(marks)

    if marks < 0 or marks > 100:
        raise ValueError("Marks must be between 0 and 100.")

except ValueError as e:
    print("Invalid Input:", e)
    exit()

try:
    with open(filename, "r") as file:
        data = file.read()

except PermissionError:
    print("Error: Permission denied.")

except Exception as e:
    print("Unexpected Error:", e)

print("Valid Input Received")
print("Marks =", marks)
