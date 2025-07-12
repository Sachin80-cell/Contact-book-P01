contacts = []

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts.append({'name': name, 'phone': phone, 'email': email, 'address': address})
    print("Contact added successfully!")

def view_contacts():
    for idx, contact in enumerate(contacts, 1):
        print(f"\nContact {idx}")
        for key, value in contact.items():
            print(f"{key.capitalize()}: {value}")

def search_contact():
    keyword = input("Enter name or phone number to search: ")
    for contact in contacts:
        if contact['name'] == keyword or contact['phone'] == keyword:
            print("\nContact Found:")
            for key, value in contact.items():
                print(f"{key.capitalize()}: {value}")
            return
    print("Contact not found!")

def update_contact():
    name = input("Enter the name of the contact to update: ")
    for contact in contacts:
        if contact['name'] == name:
            contact['phone'] = input("Enter new phone: ")
            contact['email'] = input("Enter new email: ")
            contact['address'] = input("Enter new address: ")
            print("Contact updated successfully!")
            return
    print("Contact not found!")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    for contact in contacts:
        if contact['name'] == name:
            contacts.remove(contact)
            print("Contact deleted successfully!")
            return
    print("Contact not found!")

while True:
    print("\n--- Contact Book ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        update_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        break
    else:
        print("Invalid choice! Try again.")