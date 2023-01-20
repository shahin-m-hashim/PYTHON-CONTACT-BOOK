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

## Getting Started
To use this program, you will need to have Python installed on your computer. You can download it from the official website if you do not already have it.

* Clone the repository to your local machine 
* Copy code and run it on a browser- git clone https://github.com/shahin-m-hashim/PYTHON-CONTACT-BOOK
* Or You can simply download the zip file and use it.

### On Windows,Mac or Linux 
* Navigate to the project directory
* Open up the terminal
* Type python filename.py or py filename.py to run the program
* Alternatively you can simply use any application like pycharm,vscode etc

## Usage
Once the program is running, you will be prompted with a menu that allows you to perform different actions on your contacts.

* To add a new contact, select option 1 and enter the required information.
* To remove a contact, select option 2 and enter the name of the contact you wish to remove.
* To update a contact, select option 3 and enter the name of the contact you wish to update, followed by the new information.
* To search for a contact, select option 4 and enter the name of the contact you are looking for.
* To list all contacts, select option 5.
* To exit the program, select option 6.

## Note
The program will prompt you for a valid input for phone number and email.
The program will notify you if the contact does not exist when trying to remove or update it.

## Contributing
If you find a bug or have an idea for an improvement, please open an issue or create a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
Enjoy the Contact book and keep your contacts organized(Well Logically)
Please keep in mind the drawbacks of the program before using it.
