def display_menu():
    print("Contact Book Menu:")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Edit Contact")
    print("4. Delete Contact")
    print("5. List All Contacts")
    print("6. Exit")

    return  

def add_contact(contacts):

    name = input()
    phone = input()
    email = input()
    address = input()
    contact_book = {}

 # Create inner dictionary for contact details
    contact_details = {
        "phone": phone,
        "email": email,
        "address": address
    }

    # Check if the contact already exists
    if name in contacts:
        print("Contact already exists!")
        return
    else:
        contact_book[name] = contact_details
        print("Contact added successfully!")
    return contact_book

def view_contact(contacts):
    name = input()
    if name in contacts:
        phone = contacts[name]["phone"]
        email = contacts[name]["email"]
        address = contacts[name]["address"]
        print(f"Name: {name}")
        print(f"Phone: {phone}")
        print(f"Email: {contacts[name]['email']}")
        print(f"Address: {contacts[name]['address']}")
    else:
        print("Contact not found!")
    return contacts

def edit_contact(contacts):
    name = input()
    if name in contacts:
        original_phone = contacts[name]["phone"]
        original_email = contacts[name]["email"]
        original_address = contacts[name]["address"]

# Prompt user for new details, allowing them to leave fields blank to keep original values
# If the user inputs an empty string, the original value will be retained

        phone = input()
        if phone == "":
            phone = original_phone
        email = input()
        if email == "":
            email = original_email
        address = input()
        if address == "":
            address = original_address
          
# Update the contact details in the dictionary
        contacts[name] = {
            "phone": phone,
            "email": email,
            "address": address
        }
        print("Contact updated successfully!")  
    else:
        print("Contact not found!")
    return contacts


def delete_contact(contacts):
    name = input()
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("No contacts available.")
    return contacts

def list_all_contacts(contacts):
    if not contacts:
        print("No contacts available.")
    else:
        for name, details in contacts.items():
            print(f"Name: {name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}")
            print(f"Address: {details['address']}")
            print()
    return contacts

contact_book = {}
# first_line = input()
# contact_book = eval(first_line)
while True: 
    display_menu()
    command = input()
    if command == "1":
        contact_book.update(add_contact(contact_book))
    elif command == "2":
        contact_book.update(view_contact(contact_book))
    elif command == "3":
        contact_book.update(edit_contact(contact_book))
    elif command == "4":
        contact_book.update(delete_contact(contact_book))
    elif command == "5":
            list_all_contacts(contact_book)
    elif command == "6":
        break
    else:
        print("Invalid command! Please try again.")


    

