mobile_number = {
    "ravi": "9046547810",
    "raju": "7846878944",
    "ram": "0845612794"
}

print(mobile_number)

mobile_number.update({"rahul": "8154078754"})
print(mobile_number)

name = input("Enter name to search: ").lower()

number = mobile_number.get(name)

if number:
    print("Mobile number:", number)
else:
    print("Contact not found")