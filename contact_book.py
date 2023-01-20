import re

class Contact:
    def __init__(self, name, phone_number, email, address, job):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.job = job

    def display(self):
        print(f'\nName: {self.name}')
        print(f'Phone: {self.phone_number}')
        print(f'Email: {self.email}')
        print(f'Address: {self.address}')
        print(f'Job: {self.job}')

class ContactBook:

    def __init__(self):
        self.contacts = []

    def add(self, name, phone_number, email,address,job):
        self.contacts.append(Contact(name, phone_number, email,address,job))

    def exists(self, name):
        for contact in self.contacts:
            if contact.name == name:
                return True
        return False
    
    def search(self, name):
        for contact in self.contacts:
            if contact.name == name:
                return contact
        return None

    def remove(self, name):
        if self.exists(name):
            for contact in self.contacts:
                if contact.name == name:
                    self.contacts.remove(contact)
                    print("\nContact removed!")
        else:
            print("\nContact does not exist.")

    def update(self, name, new_name=None, phone_number=None, email=None, address=None, job=None):
        if self.exists(name):
            for contact in self.contacts:
                if contact.name == name:
                    if new_name:
                        contact.name = new_name
                    if phone_number:
                        contact.phone_number = phone_number
                    if email:
                        contact.email = email
                    if address:
                        contact.address = address
                    if job:
                        contact.job = job
                    print("\nContact updated!")
        else:
            print("\nContact does not exist.")

    def list(self):
        for i, contact in enumerate(self.contacts):
            print(f'\nContact {i+1}:')
            contact.display()

def main():
    contact_book = ContactBook()
    print("\nCONTACT BOOK USING PYTHON")
    while True:
        print("\n1. Add Contact\n2. Remove Contact\n3. Update Contact\n4. Search Contact\n5. List Contacts\n6. Exit")
        choice = input("\nEnter your choice: ")
        if choice.isdigit():
            choice = int(choice)

            if choice == 1:

                name = input("\nEnter name: ").strip()
                while not name: 
                    print("Name cannot be empty. Please enter a valid name.")
                    name = input("\nEnter name: ").strip()

                phone_number = input("Enter phone number: ").strip()
                while not phone_number.isdigit(): 
                    print("\nInvalid phone number. Please enter a valid number.")
                    phone_number = input("Enter phone number: ").strip()

                email = input("Enter email: ").strip()
                while not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                    print("\nInvalid email. Please enter a valid email.")
                    email = input("Enter email: ").strip()

                address = input("Enter address: ").strip()
                job = input("Enter job: ").strip()
                contact_book.add(name, phone_number, email, address, job)

            elif choice == 2:

                name = input("\nEnter name of contact to remove: ").strip()
                while not name: 
                    print("\nName cannot be empty. Please enter a valid name.")
                    name = input("\nEnter name: ").strip()
                contact_book.remove(name)

            elif choice == 3:

                name = input("\nEnter name of contact to update: ").strip()
                new_name = input("\nEnter new name (leave blank if not updating): ").strip()
                phone_number = input("Enter new phone number (leave blank if not updating): ").strip()
                email = input("Enter new email (leave blank if not updating): ").strip()
                address = input("Enter new address (leave blank if not updating): ").strip()
                job = input("Enter new job (leave blank if not updating): ").strip()
                contact_book.update(name, new_name, phone_number, email, address, job)

            elif choice == 4:

                name = input("\nEnter name of contact to search: ").strip()
                contact = contact_book.search(name)
                if contact:
                    contact.display()
                else:
                    print("\nContact not found.")

            elif choice == 5:
                contact_book.list()

            elif choice == 6:
                break

            else:
                print("\nInvalid Option. Please enter a valid option.")
        else:
            print("\nInvalid choice. Please enter a valid number.")

if __name__ == "__main__":
    main()
