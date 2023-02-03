# CONTACT BOOK USING PYTHON
This is a Python program that allows you to manage your contacts by creating, reading, updating, and deleting them. It uses two classes, Contact and ContactBook, to store and manage the contacts.This code is a complete implementation of a Contact Book application in Python.

It contains two classes :
Contact : which has a constructor that accepts name, phone_number, email, address and job as input arguments and assigns them to the corresponding attributes of the class.
ContactBook : it has several methods such as:
* add_contact : which accepts the same input arguments as the Contact class constructor and creates a new Contact object, and appends it to the list of contacts.
* remove_contact : which accepts a contact name as input, checks if the contact exists and if it does it removes it from the contacts list.
* update_contact : which accepts the contact name, phone_number, email, address, and job as input, checks if the contact exists and if it does it updates the contact's information.
* search_contact : which accepts a contact name as input and returns the contact if it exists, otherwise returns None.<br>
* list_contacts : which prints the information of all the contacts in the contact book.<br>

The main function is used to test the classes and their methods.

The validate_integer function is used to check whether the input provided by the user is an integer or not.

The code also uses the python library 're' to check if the email provided by the user is in correct format using regular expression.

The code is well organized, easy to read, and it covers all the required functionality for a contact book application.

![An example image](https://github.com/shahin-m-hashim/PYTHON-CONTACT-BOOK/blob/main/contact_book_terminal.png)

## Features
* Add new contacts with name, phone number, email, address and job.
* Remove existing contacts
* Update existing contacts
* Search for a specific contact by name
* List all contacts

## Drawbacks
This Python program was written for learning and improving knowledge on OOPs, data validation, and basic file handling techniques.
* The program does not have a UI interface, all the interactions are done through the command line
* The program does not handle database storage, all the contacts are stored in memory and will be lost once the program is closed.
* The program does not provide a way to permanently save the contacts, they need to be exported manually to be saved.
* The program does not have a feature to sort or filter the contacts, making it difficult to navigate through a large number of contacts.

# CONTACT BOOK UI 
This Python program now includes a UI interface using the tkinter library, allowing for a more user-friendly experience. The program allows the user to add new contacts with name, phone number, email, address and job, remove existing contacts, update existing contacts, search for a specific contact by name and list all contacts. The program also includes validation for inputs such as phone number and email, ensuring that the data entered is in the correct format. However, it still does not handle database storage and the contacts will be lost once the program is closed. Additionally, there is no option to permanently save the contacts, they need to be exported manually. This version of the program is more suited for real-world use and easy to interact with.

This script defines a Contact class that stores information about a contact, including their name, phone number, email, address, and job. The script also defines a validate_integer function that checks whether a given input can be converted to an integer. The program uses two main classes: the Contact class and the ContactBook class. The Contact class is used to store the contact information, while the ContactBook class is used to manage a list of contacts. The ContactBook class has several methods that allow the user to add, update, search, and remove contacts from the list. Additionally, the program has two other classes: ListContactsWindow and UpdateContactWindow. The ListContactsWindow class opens a tkinter window that displays the list of contacts, while the UpdateContactWindow class opens a tkinter window that allows the user to update the information of a specific contact.

![An example image](https://github.com/shahin-m-hashim/PYTHON-CONTACT-BOOK/blob/main/contact_book_ui.png)

## Drawbacks
This Python program was written for learning and improving knowledge on UI interface provided by python's Tkinter library.
* The program does not have proper resizing of the UI interface.
* The program uses in-memory storage for contacts, meaning that the contacts will be lost once the program is closed.
* The program does not have a feature to sort or filter the contacts, making it difficult to navigate through a large number of contacts.

## Getting Started
To use this program, you will need to have Python installed on your computer. You can download it from the official website if you do not already have it.

* Clone the repository to your local machine 
* Copy code and run it on a browser- git clone https://github.com/shahin-m-hashim/PYTHON-CONTACT-BOOK
* Or You can simply download the zip file and use it.
* Navigate to the downloaded directory
* Open up the terminal
* For the UI to work you should have tkinter library installed, to install : pip install tk
* Type python filename.py or py filename.py to run the program
* Alternatively you can simply use any application like pycharm,vscode etc

## Usage

command line program -
Once the program is running, you will be prompted with a menu that allows you to perform different actions on your contacts.

* To add a new contact, select option 1 and enter the required information.
* To remove a contact, select option 2 and enter the name of the contact you wish to remove.
* To update a contact, select option 3 and enter the name of the contact you wish to update, followed by the new information.
* To search for a contact, select option 4 and enter the name of the contact you are looking for.
* To list all contacts, select option 5.
* To exit the program, select option 6.

ui interface program-
Once the program is running, you will be prompted with a tkinter-based UI interface that allows you to perform different actions on your contacts.

* To add a new contact, you can fill in the required information in the fields provided, such as name, phone number, email, address, and job. After you fill in the required information, can click on the "Add Contact" button to add the contact to your contact list.

* To remove a contact, you can enter the name of the contact you wish to remove in the field provided. Then click on the "Remove" button.

* To update a contact, you can enter the name of the contact you wish to update in the field provided, then fill in the new information in the fields provided and click "Update" button.

* To search for a contact, you can enter the name of the contact you are looking for in the field provided, and then click on the "Search" button.

* To list all contacts, you can click on the "List Contacts" button.

## Note
The program will prompt you for a valid input for phone number and email.
The program will notify you if the contact does not exist when trying to remove or update it.

## Contributing
If you find a bug or have an idea for an improvement, please open an issue or create a pull request.

## License
This project is licensed under the MIT License - see <a href="https://github.com/shahin-m-hashim/PYTHON-CONTACT-BOOK/blob/main/LICENSE">LICENSE.md</a>

## Acknowledgments
Enjoy the Contact book and keep your contacts organized(Well Logically)
Please keep in mind the drawbacks of the program before using it.
