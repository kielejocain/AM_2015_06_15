# Create a dictionary of dictionaries to hold your data.
phonebook = {
    'joecken': {'name': 'Kyle Joecken', 'phone': '503-555-1212'},
    'jones': {'name': 'Chris Jones', 'phone': '503-234-5678'}
    }


def add():
    # add an entry to your phonebook.
    last_name = raw_input("What is the last name of the contact? >>")
    first_name = raw_input("What is the first name? >>")
    phone = raw_input("What is their phone number? >>")
    entry = {
        'name': first_name + " " + last_name,
        'phone': phone
        }
    phonebook[last_name.lower()] = entry
    print "\nYou have added " + entry['name'] + " to your phonebook."

def edit():
    entry_to_edit = raw_input("Please enter the last name of the contact to be edited. >>").lower()
    print "You are editing the information for " + phonebook[entry_to_edit]['name']
    edit_choice = raw_input "Do you wish to enter the name(1), the number(2), or both(3)?".lower()

    if edit_choice == "1":
        phonebook[entry_to_edit]['name'] = raw_input "Enter new name. >>"
    elif edit_choice == "2":
        phonebook[entry_to_edit]['number'] == raw_input "Enter new number. >>"
    elif edit_choice == "3":
        phonebook[entry_to_edit]['name'] = raw_input "Enter new name. >>"
        phonebook[entry_to_edit]['number'] == raw_input "Enter new number. >>"
    # if a non-choice, berate the user
    else:
        print "\nThat is not a valid choice!\n"

def delete():
    # delete an entry from the phonebook if it exists.
    entry_to_delete = raw_input("Please enter the last name for the entry to be deleted. >> ")
    del phonebook[entry_to_delete.lower()]
    print "\nYou have deleted " +  entry_to_delete + " from your phonebook."

def search():
    # find and print an entry if it exists._
    entry_to_find = raw_input("Please enter the last name of the contact. >> ").lower()

    if entry_to_find in phonebook:
        print "Contact Info: %s" %(phonebook[entry_to_find])
    else:
        print "\nThat contact does not exist."


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
