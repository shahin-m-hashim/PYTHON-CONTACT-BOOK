import re
import tkinter as tk
from tkinter import messagebox

class Contact:
    def __init__(self, name, phone_number, email, address, job):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.job = job

    def display_contact(self):
        print(f'\nName: {self.name}')
        print(f'Phone Number: {self.phone_number}')
        print(f'Email: {self.email}')
        print(f'Address: {self.address}')
        print(f'Job: {self.job}')

class ContactBook:
    def __init__(self):
        self.contacts = []
    
    def add_contact(self, name, phone_number, email,address,job):
        self.contacts.append(Contact(name, phone_number, email,address,job))

    def check_contact_exists(self, name):
        for contact in self.contacts:
            if contact.name == name:
                return True
        return False
    
    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                return contact
        return None

    def remove_contact(self, name):
        if self.check_contact_exists(name):
            for contact in self.contacts:
                if contact.name == name:
                    self.contacts.remove(contact)
                    print("\nContact removed successfully!")
        else:
            print("\nContact does not exist.")

    def update_contact(self, name=None, new_name=None, phone_number=None, email=None, address=None, job=None):
        if self.check_contact_exists(name):
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
                    print("\nContact updated successfully!")
        else:
            print("\nContact does not exist.")

    def list_contacts(self):
        if self.contacts:
            counter = 1
            for contact in self.contacts:
                print(f'\nContact {counter}:')
                print(f'Name: {contact.name}')
                print(f'Phone Number: {contact.phone_number}')
                print(f'Email: {contact.email}')
                print(f'Address: {contact.address}')
                print(f'Job: {contact.job}')
                counter += 1
        else:
            print("\nNo contacts found.")

def validate_integer(number):
    try:
        int(number)
        return True
    except ValueError:
        return False

    # other methods of the ContactBook class as before

class ContactBookGUI:

    def __init__(self, master):
        self.master = master
        master.title("Contact Book")

        self.contact_book = ContactBook()

        self.name_label = tk.Label(master, text="Name:")
        self.name_label.grid(row=0, column=0)

        self.name_entry = tk.Entry(master)
        self.name_entry.grid(row=0, column=1)

        self.phone_label = tk.Label(master, text="Phone Number:")
        self.phone_label.grid(row=1, column=0)

        self.phone_entry = tk.Entry(master)
        self.phone_entry.grid(row=1, column=1)

        self.email_label = tk.Label(master, text="Email:")
        self.email_label.grid(row=2, column=0)

        self.email_entry = tk.Entry(master)
        self.email_entry.grid(row=2, column=1)

        self.address_label = tk.Label(master, text="Address:")
        self.address_label.grid(row=3, column=0)

        self.address_entry = tk.Entry(master)
        self.address_entry.grid(row=3, column=1)

        self.job_label = tk.Label(master, text="Job:")
        self.job_label.grid(row=4, column=0)
        
        self.job_entry = tk.Entry(master)
        self.job_entry.grid(row=4, column=1)

        self.add_button = tk.Button(master, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=5, column=0, columnspan=2)

        self.search_label = tk.Label(master, text="Search by Name:")
        self.search_label.grid(row=6, column=0)

        self.search_entry = tk.Entry(master)
        self.search_entry.grid(row=6, column=1)

        self.search_button = tk.Button(master, text="Search", command=self.search_contact)
        self.search_button.grid(row=7, column=0)

        self.list_button = tk.Button(master, text="List Contacts", command=self.list_contacts)
        self.list_button.grid(row=7, column=1)

        self.remove_label = tk.Label(master, text="Remove by Name:")
        self.remove_label.grid(row=8, column=0)

        self.remove_entry = tk.Entry(master)
        self.remove_entry.grid(row=8, column=1)

        self.remove_button = tk.Button(master, text="Remove", command=self.remove_contact)
        self.remove_button.grid(row=9, column=0)

        self.update_label = tk.Label(master, text="Update by Name:")
        self.update_label.grid(row=9, column=1)

        self.update_entry = tk.Entry(master)
        self.update_entry.grid(row=10, column=1)

        self.update_button = tk.Button(master, text="Update", command=self.update_contact)
        self.update_button.grid(row=10, column=0)

    def add_contact(self):
        name = self.name_entry.get()
        phone_number = self.phone_entry.get()
        email = self.email_entry.get()

        if not name or not phone_number or not email:
            messagebox.showerror("Error", "Name, Phone Number and Email are required!")
            return

        if not validate_integer(phone_number):
            messagebox.showerror("Error", "Invalid Phone Number")
            return

        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            messagebox.showerror("Error", "Invalid Email")
            return

        address = self.address_entry.get()
        job = self.job_entry.get()
        self.contact_book.add_contact(name, phone_number, email, address, job)
        messagebox.showinfo("Success", "Contact added successfully!")

    def remove_contact(self):
        name = self.remove_entry.get()
        if not name:
            messagebox.showerror("Error", "Name field is required!")
            return
        if not self.contact_book.check_contact_exists(name):
            messagebox.showerror("Error", "Contact does not exist!")
            return
        self.contact_book.remove_contact(name)
        messagebox.showinfo("Success", "Contact removed successfully!")


    def update_contact(self):
        name = self.name_entry.get()
        new_name = self.new_name_entry.get()
        phone_number = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()
        job = self.job_entry.get()

        if not name:
            messagebox.showerror("Error", "Current name field is required!")
            return
        
        if new_name:
            name = new_name

        if not self.contact_book.check_contact_exists(name):
            messagebox.showerror("Error", "Contact does not exist!")
            return

        if not validate_integer(phone_number):
            messagebox.showerror("Error", "Invalid Phone Number")
            return

        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            messagebox.showerror("Error", "Invalid Email")
            return
            
        self.contact_book.update_contact(name, new_name=new_name, phone_number=phone_number, email=email, address=address, job=job)
        messagebox.showinfo("Success", "Contact updated successfully!")

    def search_contact(self):
        name = self.search_entry.get()
        if not name:
            messagebox.showerror("Error", "Name field is required!")
        else:
            contact = self.contact_book.search_contact(name)
            if contact:
                messagebox.showinfo("Contact Found", f'Name: {contact.name}\nPhone Number: {contact.phone_number}\nEmail: {contact.email}\nAddress: {contact.address}\nJob: {contact.job}')
            else:
                messagebox.showerror("Error", "Contact not found!")


    def list_contacts(self):
        contacts = self.contact_book.list_contacts()
        if contacts:
            message = ""
            for i in range(len(contacts)):
                message += f'\nContact {i+1}:\n'
                message += f'Name: {contacts[i].name}\n'
                message += f'Phone Number: {contacts[i].phone_number}\n'
                message += f'Email: {contacts[i].email}\n'
                message += f'Address: {contacts[i].address}\n'
                message += f'Job: {contacts[i].job}\n'
            messagebox.showinfo("Contacts", message)
        else:
            messagebox.showerror("Error", "No contacts found!")

def main():
  root = tk.Tk()
  gui = ContactBookGUI(root)
  root.mainloop()
    
if __name__ == "__main__":
    main()

