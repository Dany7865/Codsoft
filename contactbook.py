contacts = {}
def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts[name] = {"Phone": phone, "Email": email, "Address": address}
    print("Contact added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts to display.")
    else:
        for name, info in contacts.items():
            print(f"\nName: {name}")
            print(f"Phone: {info['Phone']}")
            print(f"Email: {info['Email']}")
            print(f"Address: {info['Address']}")

def search_contact():
    keyword = input("Enter name or phone number to search: ").lower()
    found = False
    for name, info in contacts.items():
        if keyword in name.lower() or keyword in info['Phone']:
            print(f"\nName: {name}")
            print(f"Phone: {info['Phone']}")
            print(f"Email: {info['Email']}")
            print(f"Address: {info['Address']}")
            found = True
    if not found:
        print("Contact not found.")

def update_contact():
    name = input("Enter the name of the contact to update: ")
    if name in contacts:
        phone = input("Enter new phone number: ")
        email = input("Enter new email: ")
        address = input("Enter new address: ")
        contacts[name] = {"Phone": phone, "Email": email, "Address": address}
        print("Contact updated successfully!")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

def menu():
    while True:
        print("\n----- Contact Book -----")
        print("1. Add Contact")
        print("2. View Contacts List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Choose an option (1-6): ")
        
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
            print("Thanku and Goodbye!")
            break
        else:
            print("Invalid . Try again.")


menu()