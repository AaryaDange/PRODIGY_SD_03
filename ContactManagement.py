import json
import os

class ContactManager:
    def __init__(self, filename='contacts.json'):
        self.filename = filename
        self.contacts = self.load_contacts()

    def load_contacts(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return json.load(file)
        return {}

    def save_contacts(self):
        with open(self.filename, 'w') as file:
            json.dump(self.contacts, file, indent=4)

    def add_contact(self, name, phone, email):
        self.contacts[name] = {'phone': phone, 'email': email}
        self.save_contacts()
        print(f"Contact {name} added.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            for name, info in self.contacts.items():
                print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")

    def edit_contact(self, name):
        if name in self.contacts:
            phone = input("Enter new phone number: ")
            email = input("Enter new email address: ")
            self.contacts[name] = {'phone': phone, 'email': email}
            self.save_contacts()
            print(f"Contact {name} updated.")
        else:
            print(f"Contact {name} not found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            self.save_contacts()
            print(f"Contact {name} deleted.")
        else:
            print(f"Contact {name} not found.")

    def run(self):
        while True:
            print("\nContact Manager")
            print("1. Add Contact")
            print("2. View Contacts")
            print("3. Edit Contact")
            print("4. Delete Contact")
            print("5. Exit")

            choice = input("Choose an option: ")

            if choice == '1':
                name = input("Enter name: ")
                phone = input("Enter phone number: ")
                email = input("Enter email address: ")
                self.add_contact(name, phone, email)
            elif choice == '2':
                self.view_contacts()
            elif choice == '3':
                name = input("Enter name of the contact to edit: ")
                self.edit_contact(name)
            elif choice == '4':
                name = input("Enter name of the contact to delete: ")
                self.delete_contact(name)
            elif choice == '5':
                print("Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")

if __name__ == '__main__':
    manager = ContactManager()
    manager.run()
