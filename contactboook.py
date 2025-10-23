contacts = {}

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts[name] = {"phone": phone, "email": email, "address": address}
    print("Contact added!")

def view_contact():
    for name, info in contacts.items():
        print(f"\nName: {name}")
        print(f"Phone: {info['phone']}")
        print(f"Email: {info['email']}")
        print(f"Address: {info['address']}")

def search_contact():
    search = input("Enter name or phone to search: ")
    for name, info in contacts.items():
        if search in name or search in info['phone']:
            print(f"\nFound: {name} - {info}")

def delete_contact():
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted.")
    else:
        print("Contact not found.")

while True:
    print("\n--- Contact Book ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")
    
    choice = input("Enter choice: ")
    
    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contact()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        break
    else:
        print("Invalid choice.")
