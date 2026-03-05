num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))

print("Select operation: +, -, *, /, %, **")
operation = input("Enter operation: ")

if operation == '+':
    print(num1 + num2)
elif operation == '-':
    print(num1 - num2)
elif operation == '*':
    print(num1 * num2)
elif operation == '/':
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        print(num1 / num2)
elif operation == '%':
    print(num1 % num2)
elif operation == '**':
    print(num1 ** num2)
else:
    print("Invalid operation")
