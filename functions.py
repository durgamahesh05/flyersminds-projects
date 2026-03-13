# finding simple interest by using simple_interest function
def simple_interest():
    p = float(input("Enter the principal amount: "))
    r = float(input("Enter the rate of interest: "))
    t = float(input("Enter the time period in years: "))
    si = (p * r * t) / 100
    print(f"The simple interest is: {si}")
simple_interest()


#finding the area of circle using the function

def Area_ofcircle():
    radius = float(input("Enter the radius of the circle: "))
    area = 3.14159 * radius ** 2
    print(f"The area of the circle with radius {radius} is: {area}")
Area_ofcircle()




# finding the factorial of a number by using factorial function
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result


# checking if the word is a palindrome or not by using palindrome_check function
def palindrome_check():
    word = input("enter a word:")
    if word == word[::-1]:
        print(f"{word} is a palindrome.")
    else:
        print(f"{word} is not a palindrome.")
palindrome_check()


#even or odd number checker by using check_number function
def check_number():
    try:
        num = int(input("Enter a number: "))
        if num % 2 == 0:
            print(f"{num} is an even number.")
        else:
            print(f"{num} is an odd number.")
    except ValueError:
        print("Invalid input. Please enter an integer.")

check_number()