contact = {}
while True:
    print("\n----contact book----")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")
    choice = input("Enter your choice here (from 1-5): ")

    if choice == '1':
        name = input("Enter contact name: ")
        phone = input("Enter contact phone number: ")
        contact[name] = phone
        print(f"Contact {name} added successfully.")

    elif choice == '2':
        if contact:
            print("\nsaved contacts: ")
            for name , phone in contact.items():
                print(name, ":", phone)
        else:
            print("No contacts found.")

    elif choice == '3':
        name =input("ENter contact name to search: ")
        if name in contact:
            print(f"{name} : {contact[name]}")
        else:
            print(f"contact {name} not found")

    elif choice == '4':
        name = input("Enter contact name to delete: ")
        if name in contact:
            del contact[name]
            print(f"contact {name} deleted successfully")
        else:
            print(f"contact {name} not found")

    elif choice == '5':
        print("Thnak you for using the contact book ")
        break
    else:
        print("Invalid choice. Please try again ")