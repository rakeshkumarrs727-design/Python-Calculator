contacts = {}

while True:
    print("\n---- Contact Book System ----")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # Add Contact
    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        contacts[name] = phone
        print("Contact added successfully!")

    # View Contacts
    elif choice == "2":
        if contacts:
            print("\nSaved Contacts:")
            for name, phone in contacts.items():
                print(name, ":", phone)
        else:
            print("No contacts found.")

    # Search Contact
    elif choice == "3":
        search = input("Enter name to search: ")
        if search in contacts:
            print("Phone number:", contacts[search])
        else:
            print("Contact not found.")

    # Delete Contact
    elif choice == "4":
        delete = input("Enter name to delete: ")
        if delete in contacts:
            del contacts[delete]
            print("Contact deleted.")
        else:
            print("Contact not found.")

    # Exit
    elif choice == "5":
        print("Exiting Contact Book...")
        break

    else:
        print("Invalid choice. Try again.")
