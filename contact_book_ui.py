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
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                return
        messagebox.showerror('Error', 'Contact not found')


    def update_contact(self, name, contact):
        for c in self.contacts:
            if c.name == name:
                c.name = contact.name
                c.phone = contact.phone
                c.email = contact.email
                c.address = contact.address
                c.job = contact.job
                return
        messagebox.showerror('Error', 'Contact not found')

    def list_contacts(self):
        if not self.contacts:
            messagebox.showerror('Error', 'No contacts found')
        else:
            contact_list = ''
            for i, contact in enumerate(self.contacts):
                contact_list += str(i+1) + '. ' + contact.name + '\n'
            messagebox.showinfo('Contact List', contact_list)

def validate_integer(number):
    try:
        int(number)
        return True
    except ValueError:
        return False

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Contact Book')
        self.root.geometry('850x450')

        self.contact_book = ContactBook()

        self.name_label = tk.Label(self.root, text='Name:')
        self.name_label.grid(row=0, column=0, pady=5)
        self.name_label.config(font=super)
        self.name_entry = tk.Entry(self.root, width=50)
        self.name_entry.grid(row=0, column=1,pady=5)

        self.phone_label = tk.Label(self.root, text='Phone:')
        self.phone_label.grid(row=1, column=0,pady=5)
        self.phone_label.config(font=super)
        self.phone_entry = tk.Entry(self.root, width=50 )
        self.phone_entry.grid(row=1, column=1,pady=5)

        self.email_label = tk.Label(self.root, text='Email:')
        self.email_label.grid(row=2, column=0,pady=5)
        self.email_label.config(font=super)
        self.email_entry = tk.Entry(self.root, width=50)
        self.email_entry.grid(row=2, column=1,pady=5)

        self.address_label = tk.Label(self.root, text='Address:')
        self.address_label.grid(row=3, column=0,pady=5)
        self.address_label.config(font=super)
        self.address_entry = tk.Entry(self.root, width=50)
        self.address_entry.grid(row=3, column=1,pady=5)

        self.job_label = tk.Label(self.root, text='Job:')
        self.job_label.grid(row=4, column=0,pady=5)
        self.job_label.config(font=super)
        self.job_entry = tk.Entry(self.root, width=50)
        self.job_entry.grid(row=4, column=1,pady=5)

        self.add_button = tk.Button(self.root, text='Add Contact ', command=self.add_contact,width=30)
        self.add_button.grid(row=5, column=0,padx=10,pady=20)
        self.add_button.config(background='#7CFC00',highlightbackground='black', bd=3)

        self.list_button = tk.Button(self.root, text='List Contacts ', command=self.list_contacts,width=30)
        self.list_button.grid(row=5, column=1,pady=20)
        self.list_button.config(background='#7CFC00',highlightbackground='black', bd=3)

        self.name_label = tk.Label(self.root, text='Remove Contact by name ',padx=0,pady=10)
        self.name_label.grid(row=6, column=0)
        self.remove_entry = tk.Entry(self.root,width=30)
        self.remove_entry.grid(row=6, column=1)
        self.remove_button = tk.Button(self.root, text=' Remove ', command=self.remove_contact,width=10,padx=5)
        self.remove_button.config(background='yellow',highlightbackground='black', bd=2)
        self.remove_button.grid(row=6, column=2,padx=20)

        self.name_label = tk.Label(self.root, text='Search Contact by name ',padx=0,pady=10)
        self.name_label.grid(row=7, column=0)
        self.search_entry = tk.Entry(self.root,width=30)
        self.search_entry.grid(row=7, column=1)
        self.search_button = tk.Button(self.root, text=' Search ', command=self.search_contact,width=10,padx=5)
        self.search_button.config(background='yellow',highlightbackground='black', bd=2)
        self.search_button.grid(row=7, column=2,padx=20)

        self.name_label = tk.Label(self.root, text='Update Contact by name ',padx=0,pady=20)
        self.name_label.grid(row=8, column=0)
        self.update_entry = tk.Entry(self.root,width=30)
        self.update_entry.grid(row=8, column=1)
        self.update_button = tk.Button(self.root, text=' Update ', command=self.update_contact,width=10,padx=5)
        self.update_button.config(background='yellow',highlightbackground='black', bd=2)
        self.update_button.grid(row=8, column=2,padx=20)


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

    def update_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()
        job = self.job_entry.get()
        if name and phone and email:
            contact = Contact(name, phone, email, address, job)
            self.contact_book.update_contact(name, contact)
            messagebox.showinfo('Success', 'Contact updated')
        else:
            messagebox.showerror('Error', 'Name, Phone and Email are required')

    def list_contacts(self):
        self.contact_book.list_contacts()

    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    app = App()
    app.run()
