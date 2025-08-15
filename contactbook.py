contacts = []

while True:
    print("\n Contact Book")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Search Contact")
    print("4. Remove Contact")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        contact = {
            "name": name,
            "phone": phone
        }
        contacts.append(contact)
        print("Contact added successfully.")

    elif choice == "2":
        if contacts:
            print("\nContacts:")
            for i, contact in enumerate(contacts, start=1):
                print(f"{i}. {contact['name']} - {contact['phone']}")
        else:
            print("No contacts available.")
            print("Please add a contact first.")
    
    elif choice == "3":
        search_name = input("Enter name to search: ")
        found = False
        for contact in contacts:
            if contact['name'].lower() == search_name.lower():
                print(f"Found contact: {contact['name']} - {contact['phone']}")
                found = True
                break
        if not found:
            print("Contact not found.")

    elif choice == "4":
        remove_name = input("Enter name to remove: ")
        for i, contact in enumerate(contacts):
            if contact['name'].lower() == remove_name.lower():
                del contacts[i]
                print("Contact removed successfully.")
                break
        else:
            print("Contact not found.")

    elif choice == "5":
        print("Exiting Contact Book.")
        break

    else:
        print("Invalid choice. Please try again.")

