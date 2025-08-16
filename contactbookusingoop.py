class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone


class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        for contact in self.contacts:
            print(f"Name: {contact.name}, Phone: {contact.phone}")


# Create objects
contact1 = Contact("Pradeep", "1234567890")
contact2 = Contact("Anjali", "987654321")

# Create a contact book
book = ContactBook()

# Add contacts
book.add_contact(contact1)
book.add_contact(contact2)

# View contacts
book.view_contacts()

