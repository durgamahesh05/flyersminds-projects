import json
import os

class Student:
    def __init__(self, name, roll_number, age):
        self.name = name
        self.roll_number = roll_number
        self.age = age

    def display_info(self):
        print(f"Name : {self.name}")
        print(f"Roll No : {self.roll_number}")
        print(f"Age : {self.age}")
        print("-" * 30)

    def to_dict(self):
        return {
            "name": self.name,
            "roll_number": self.roll_number,
            "age": self.age
        }


class ManagementSystem:
    def __init__(self):
        self.file_name = "students.json"
        self.student_list = []
        self.load_data()

    def load_data(self):
        if os.path.exists(self.file_name):
            with open(self.file_name, "r") as file:
                data = json.load(file)

                for student in data:
                    obj = Student(
                        student["name"],
                        student["roll_number"],
                        student["age"]
                    )
                    self.student_list.append(obj)

    def save_data(self):
        data = [student.to_dict() for student in self.student_list]

        with open(self.file_name, "w") as file:
            json.dump(data, file, indent=4)

    def add_student(self):
        name = input("Enter Name: ")
        roll_number = input("Enter Roll Number: ")
        age = input("Enter Age: ")

        student = Student(name, roll_number, age)
        self.student_list.append(student)

        self.save_data()
        print("Student Added Successfully")

    def view_students(self):
        if not self.student_list:
            print("No Students Found")
            return

        for student in self.student_list:
            student.display_info()

    def update_student(self):
        roll_number = input("Enter Roll Number to Update: ")

        for student in self.student_list:
            if student.roll_number == roll_number:
                student.name = input("Enter New Name: ")
                student.age = input("Enter New Age: ")

                self.save_data()
                print("Student Updated Successfully")
                return

        print("Student Not Found")

    def delete_student(self):
        roll_number = input("Enter Roll Number to Delete: ")

        for student in self.student_list:
            if student.roll_number == roll_number:
                self.student_list.remove(student)

                self.save_data()
                print("Student Deleted Successfully")
                return

        print("Student Not Found")


system = ManagementSystem()

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        system.add_student()

    elif choice == "2":
        system.view_students()

    elif choice == "3":
        system.update_student()

    elif choice == "4":
        system.delete_student()

    elif choice == "5":
        print("Exiting Program")
        break

    else:
        print("Invalid Choice")