import json

class Student:
    def __init__(self, name, student_id, major):
        self.name = name
        self.student_id = student_id
        self.major = major

    def to_dict(self):
        """Converts object attributes to a dictionary for JSON storage."""
        return {"name": self.name, "id": self.student_id, "major": self.major}

class StudentManager:
    def __init__(self, filename="students.json"):
        self.filename = filename

    def save_students(self, students):
        """Writes a list of Student objects to a file."""
        data = [s.to_dict() for s in students]
        with open(self.filename, "w") as f:
            json.dump(data, f, indent=4)
        print(f"Successfully saved {len(students)} students to {self.filename}.")

    def load_students(self):
        """Reads students from a file and returns a list of dictionaries."""
        try:
            with open(self.filename, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return []

s1 = Student("Marcus", "A101", "Computer Science")
s2 = Student("Saira", "B202", "Physics")


manager = StudentManager()
manager.save_students([s1, s2])

retrieved_data = manager.load_students()

print("\nRetrieved Student Records:")
for entry in retrieved_data:
    print(f"ID: {entry['id']} | Name: {entry['name']} | Major: {entry['major']}")