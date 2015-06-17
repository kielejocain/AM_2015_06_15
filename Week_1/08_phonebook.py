# Create a dictionary of dictionaries to hold your data.
phonebook = {
    'joecken': {'name': 'Kyle Joecken', 'phone': '503-555-1212'},
    'jones': {'name': 'Chris Jones', 'phone': '503-234-5678'}
    }


def add():
    # add an entry to your phonebook.
    first_name = raw_input("First name? ")
    last_name = raw_input("Last name? ")
    while last_name.lower() in phonebook:
        print "That last name is already in the phonebook."
        print "Please choose a different last name"
        last_name = raw_input("Last name? ")
    phone = raw_input("Phone number? ")
    entry = {
        'name': ' '.join([first_name, last_name]),
        'phone': phone
    }
    phonebook[last_name.lower()] = entry

def edit():
    # change an entry in your phonebook.  Use del if necessary!
    target = raw_input("Enter the last name of the entry to edit: ").lower()
    if target in phonebook:
        print phonebook[target]['name'], phonebook[target]['phone']
        print "What do you want to edit?"
        option = 0
        while option != 1 and option != 2:
            option = int(raw_input("Enter 1 to edit the name or 2 to edit the phone number: "))
        if option == 1:
            new_first_name = raw_input("New contact first name? ")
            new_last_name = raw_input("New contact last name? ")
            key_name = new_last_name.lower()
            phonebook[key_name] = {
                'name': " ".join([new_first_name, new_last_name]),
                'phone': phonebook[target]['phone']
            }
            del phonebook[target]
            print "contact is now:", phonebook[key_name]['name'], phonebook[key_name]['phone']

        else:
            new_number = raw_input("New phone number?")
            del phonebook[target]['phone']
            phonebook[target]['phone'] = new_number
            print "new contact number for", phonebook[target]['name'], "is", new_number

    else:
        print "error: name not found"


def delete():
    # delete an entry from the phonebook if it exists.
    target = raw_input("Enter the last name of the entry to delete: ").lower()
    if target in phonebook:
        print "deleted", phonebook[target]['name'], phonebook[target]['phone']
        del phonebook[target]

    else:
        print "error: name not found"


def search():
    # find and print an entry if it exists.
    target = raw_input("Enter the last name of the entry to search for: ").lower()
    if target in phonebook:
        print "found:", phonebook[target]['name'], phonebook[target]['phone']
    else:
        print "error: name not found"

# MAIN LOOP
# keep track of whether or not we're done
done = False
while not done:
    # ask the user which they'd like to do
    choice = raw_input("""
    Please make a selection.
    \t1. Search the phonebook
    \t2. Add a contact
    \t3. Edit a contact
    \t4. Delete a contact
    \t5. Exit
    Enter the number of your choice. >> """)
    # call the function chosen
    if choice == '1':
        search()
    elif choice == '2':
        add()
    elif choice == '3':
        edit()
    elif choice == '4':
        delete()
    # if done, we say so
    elif choice == '5':
        done = True
    # if a non-choice, berate the user
    else:
        print "\nThat is not a valid choice!\n"
