def add_contact(contact):
    name = input("Please type your name: ")
    number = int(input("Please type your phone number: "))
    contact[name] = number

def remove_contact(contact):
    print(contact)
    name = input("Please type your name u want to remove: ")
    contact.pop(name)

def edit_contact(contact):
    print(contact)
    name = input("Which name would you like to edit:? ")
    if name in contact:
        number = int(input(f"Enter a new number: For {name}\n"))
        contact.update({name: number})
        print(f"This phone number was assigned to this name:  {name}")
    else:
        print("Name not found! Retard_!")

def all_contacts(contact):
    if contact:
        print("Contacts list:")
        for name, number in contact.items():
            print(f"Name: {name}, Phone: {number}")
    else:
        print("No contacts found.")
def main():
  contact = {}
  while True:
    print("""
    Welcome to my contact list!
    """)


    select = int(input("1. Add Contact\n2. Remove contact\n3. Edit Contact\n4. all contacts\n5. exit\n\nType here: "))
    if select == 1:
        add_contact(contact)
        print(contact)
    elif select == 2:
        remove_contact(contact)
        print(contact)
    elif select == 3:
        edit_contact(contact)
    elif select == 4:
        all_contacts(contact)
    else:
        print("HOHO")
        break

main()