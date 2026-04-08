class Person:
    def __init__(self, name, age, city):
        """Initializes the person's attributes."""
        self.name = name
        self.age = age
        self.city = city

    def print_profile(self):
        """Prints a formatted profile of the person."""
        print("--- User Profile ---")
        print(f"Name: {self.name}")
        print(f"Age:  {self.age}")
        print(f"City: {self.city}")
        


user1 = Person("Alice", 28, "New York")
user1.print_profile()