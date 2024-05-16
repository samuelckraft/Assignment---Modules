
def add_contact(contacts):
    new_contact = input('Please enter the first and last name of the contact you want to add: ')
    contacts.append(new_contact)

def remove_contact(contacts):
    contact_to_remove = input('Please enter the first and last name of the contact you want to remove: ')
    if contact_to_remove in contacts:
        contacts.remove(contact_to_remove)
    else:
        print('Contact not found')

def view_contacts(contacts):
    print('Contacts:')
    for contact in contacts:
        print(f"- {contact}")
