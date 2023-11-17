contacts = {}

def add_contact(name,phone,e_mail):
    contacts[name] = {'Phone': phone, 'E-mail': e_mail}
    print(f'Contact {name} added successfully.')

def view_contact(name ):
    if name in contacts:
        contact_info=contacts
        print(name,"'s contact number is: ",contacts[name])
    else:
        print(f'contact {name} not found')

def display_contact(name):
    if not  contacts:
        print("Contact Book is empty")
    else:
        print("Contact list: ")
        for name, contact_info in contacts.items():
            print(f'{name}: {contact_info["Phone"]},{contact_info["E-mail"]}')

def edit_contact( name):
    if name in contacts:
        print(f'Editing contact: {name}')
        new_phone = input('Enter new phone number: ')
        new_email = input('Enter new email address: ')
        contacts[name]['Phone'] = new_phone
        contacts[name]['E-mail'] = new_email
        print(f'Contact {name} updated successfully.')
    else:
        print(f'Contact {name} not found.')

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f'Contact {name} deleted successfully.')
    else:
        print(f'Contact {name} not found.')

while True:
    print('\nContact Book Menu:')
    print('1. Add Contact')
    print('2. View Contact')
    print('3. Edit Contact')
    print('4. Show Contact List')
    print('5. Delete Contact')
    print('6. Exit')

    choice = input('Enter your choice: ')

    if choice == '1':
        name = input('Enter contact name: ')
        phone = input('Enter contact phone number: ')
        email = input('Enter contact email address: ')
        add_contact(name, phone, email)

    elif choice == '2':
        name = input('Enter contact name to view: ')
        view_contact(name)

    elif choice == '3':
        name = input('Enter contact name to edit: ')
        edit_contact(name)

    elif choice == '4':
        display_contact(name)

    elif choice == '5':
        name = input('Enter contact name to delete: ')
        delete_contact(name)

    elif choice == '6':
        print('Exiting Contact Book. Goodbye!')
        break

    else:
        print('Invalid choice. Please enter a valid option.')









