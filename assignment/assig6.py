"""
Python Assignment - Functions, *args, and **kwargs
You have learned how function work, how to use *args and **kwargs, and how to create a simple student management system. 
Now, complete the following tasks:
Write each program seperately.


"""
# 1. Sum using *args
"""
write a function total_sum() that takes any amount of numbers using *args and prints the total.
Example output:
total_sum(5,10,2,3)
20
"""
# def total_sum(*args):
#     print(sum(args))

# total_sum(5,10,2,3)
# print("\n")

# 2. Display user profile using **kwargs
""""
write a function called show_profile() that takes any user information using **kwargs and prints it in this format:

name -> ram
age -> 22
city -> Pokhara

you can call it like:
show_profile(name="ram", age=22, city="Pokhara")

"""
# def show_profile(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key} -> {value}")

# show_profile(name="ram", age=22, city="Pokhara")

# 3. Create a contact book
""""
Create a program with the following menu:
1. Add Contact
2. show contacts
3. remove contact
4. quit

each contact must store:
. name
. phone
. email
use a list of dictionaries to store the data - similar to the student program you learned in class.

"""

# contact_book = []  # list of dictionaries to store contact information

# while True:   
#     print("1. Add Contact")
#     print("2. show contacts")
#     print("3. remove contact")
#     print("4. quit")

#     user_choice = input("Enter your choice (1/2/3/4) >>> ")

#     if user_choice == "1":
#         name = input("Enter name: ")
#         phone = input("Enter phone: ")
#         email = input("Enter email: ")
#         contact = {"name": name, "phone": phone, "email": email}
#         contact_book.append(contact)

#     elif user_choice == "2":
#         for contact in contact_book:
#             print(f"Name: {contact['name']}")
#             print(f"Phone: {contact['phone']}")
#             print(f"Email: {contact['email']}")
#             print("--------------------")

#     elif user_choice == "3":
#         name_to_remove = input("Enter name to remove: ")
#         for contact in contact_book:
#             if contact["name"] == name_to_remove:
#                 contact_book.remove(contact)
#                 break

#     elif user_choice == "4":
#         print("Thank you for using our program")
#         break 

#     else:
#         print("Invalid input ! Please read the instructions carefully ")  

#     print("\n")

# 4. Count Students based on age
"""
using student list from class:
. ASk the user: "Enter age:"
. then print how many students are older than that age

Example:
Enter age:18
output : 4 students are older than 18.

"""
# # Example list of student ages
# student_ages = [17, 18, 19, 20, 21, 22, 18, 23]
# # Ask the user for an age
# age = int(input("Enter age: "))
# # Count how many students are older
# count = sum(1 for a in student_ages if a > age)
# print(f"{count} students are older than {age}.")


# 5. update student data (New feature)
"""
Add a new option to your student program:
. update student data

when updating 
.ask for the student name
.if found, ask whether they want to update "name" or "age" 
.update the dictionary values

"""
# Student dictionary
contacts = {}
students = {"Ram": 20, "Ali": 18, "Sara": 22}

while True:
    print("\n1. Add Contact")
    print("2. Show Contacts")
    print("3. Remove Contact")
    print("4. Update Student Data")
    print("Q. Quit")

    choice = input("Enter choice: ").upper()

    # Add contact
    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        email = input("Enter email: ")
        contacts[name] = {"phone": phone, "email": email}
        print("Contact added.")

    # Show contacts
    elif choice == "2":
        for name, info in contacts.items():
            print(name, "-", info["phone"], "-", info["email"])

    # Remove contact
    elif choice == "3":
        name = input("Enter name to remove: ")
        if name in contacts:
            del contacts[name]
            print("Contact removed.")
        else:
            print("Contact not found.")

    # Update student data (NEW)
    elif choice == "4":
        name = input("Enter student name to update: ")

        if name in students:
            print("1. Update Name")
            print("2. Update Age")
            option = input("Choose: ")

            if option == "1":
                new_name = input("Enter new name: ")
                students[new_name] = students.pop(name)
                print("Name updated.")

            elif option == "2":
                new_age = int(input("Enter new age: "))
                students[name] = new_age
                print("Age updated.")

            else:
                print("Invalid option.")
        else:
            print("Student not found.")

    # Quit
    elif choice == "Q":
        break

    else:
        print("Invalid choice.")
