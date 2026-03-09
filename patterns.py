x = input("enter the symbol or a number u want: ")

if x.isdigit():
    rows = int(x)
else:
    rows = int(input("Enter the number of rows: "))

for i in range(1, rows + 1):
    for j in range(i):
        print(x, end=" ")
    print()