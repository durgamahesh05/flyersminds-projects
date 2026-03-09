import random

x = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9])
guess = int(input("enter the number of ypour choice: "))

if guess == x:
    print("Matched", x)
else:
    print("Not matched", x)