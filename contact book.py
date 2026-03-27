"""
Contact Book Application (CLI)
Features:
- Add Contact
- View Contacts
- Search Contact
- Update Contact
- Delete Contact
- Save & Load from file (JSON)
"""

import json

CONTACT_FILE = "contacts.json"


def load_contacts():
    try:
        with open(CONTACT_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


def save_contacts(contacts):
    with open(CONTACT_FILE, "w") as f:
        json.dump(contacts, f, indent=4)


def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")

    contacts[name] = {
        "phone": phone,
        "email": email
    }
    print("Contact added successfully!\n")


def view_contacts(contacts):
    if not contacts:
        print("No contacts found.\n")
        return

    for name, info in contacts.items():
        print(f"Name: {name}")
        print(f"Phone: {info['phone']}")
        print(f"Email: {info['email']}")
        print("-" * 30)


def search_contact(contacts):
    name = input("Enter name to search: ")
    if name in contacts:
        info = contacts[name]
        print(f"Found: {name}")
        print(f"Phone: {info['phone']}")
        print(f"Email: {info['email']}\n")
    else:
        print("Contact not found.\n")


def update_contact(contacts):
    name = input("Enter name to update: ")
    if name in contacts:
        phone = input("Enter new phone: ")
        email = input("Enter new email: ")
        contacts[name] = {"phone": phone, "email": email}
        print("Contact updated!\n")
    else:
        print("Contact not found.\n")


def delete_contact(contacts):
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted!\n")
    else:
        print("Contact not found.\n")


def main():
    contacts = load_contacts()

    while True:
        print("\n==== Contact Book ====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Save & Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            save_contacts(contacts)
            print("Contacts saved. Exiting...")
            break
        else:
            print("Invalid choice. Try again.\n")


if __name__ == "__main__":
    main()
