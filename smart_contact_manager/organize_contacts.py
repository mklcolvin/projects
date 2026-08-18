def organize_contacts(contact_list):
    # Your solution here
    
    cleaned_contacts = []   # List to store the cleaned contacts

    # 1. Create helper functions for validation
    # - Function to validate email format
    # - Function to clean and validate phone numbers
    
    # 2. Process each contact
    # - Clean email (lowercase) and phone (digits only)
    # - Check if email and phone are valid
    # - Check for duplicates
    
    # 3. Return the clean contact list

    def validate_email_format(email):
        # Simple email validation (you can expand this as needed)
        return "@" in email and "." in email.split("@")[1] and " " not in email
    
    def lowercase_email(email):
        return email.lower()

    def clear_phone(phone):
        # Remove all non-digit characters
        return "".join(filter(str.isdigit, phone))

    def is_duplicate(contact, comparison_list):
        for c in comparison_list:
            if c["email"] == contact["email"] or c["phone"] == contact["phone"]:
                return True
        return False
    

    for contact in contact_list:
        # Clean and validate email
        clean_email = lowercase_email(contact["email"])
        if not validate_email_format(clean_email):
            continue

        # Clean phone number
        clean_phone = clear_phone(contact["phone"])
        if len(clean_phone) != 10:
            continue

        test = {
                "name": contact["name"],
                "email": clean_email,
                "phone": clean_phone
            }

        # Check for duplicates
        if is_duplicate(test, cleaned_contacts):
            continue


        # Add the cleaned contact to the new list
        cleaned_contacts.append(test)

    return cleaned_contacts



contacts = [{"name": "John Doe", "email": "JOHN@email.com", "phone": "123-456-7890"}, {"name": "Jane Doe", "email": "jane@email.com", "phone": "123.456.7890"}, {"name": "Bob Smith", "email": "invalid.email", "phone": "12345"}]
new_contacts = organize_contacts(contacts)
print(new_contacts)