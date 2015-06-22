# Create a dictionary of dictionaries to hold your data.
phonebook = {
                'joecken': {'name': 'Kyle Joecken', 'phone': '503-555-1212'},
                'jones': {'name': 'Chris Jones', 'phone': '503-234-5678'}
            }


def add():
    # keep track of whether or not we've finished adding
    added = False
    while not added:
        # get the last name
        last = raw_input("Please enter the last name of the new contact.\n>> ")
        # if a contact with that name exists,
        if last.lower() in phonebook:
            # say so,
            print "\nThis contact already exists!\n"
            # offer a second chance.  If unwanted, we're done
            if raw_input("Try again? y/n >> ") != 'y':
                added = True
        # if no such contact exists,
        else:
            # get the rest of the info
            first = raw_input("Please enter the first name of the contact.\n>> ")
            phone = raw_input("Please enter the phone number of the contact.\n>> ")
            # and save it.
            phonebook[last.lower()] = {'name': first + " " + last, 'phone': phone}
            # we're done now.
            added = True


def edit():
    # This loop runs forever, or until broken with a `break` command.
    while True:
        # get the last name
        last = raw_input("What is the contact's last name?\n>> ")
        # if no such contact exists,
        if last.lower() not in phonebook:
            # say so
            print "\nNo such contact exists?\n"
            # offer a second chance. If unwanted, we're done
            if raw_input("Try again? y/n >> ") != 'y':
                break
        # if the contact does exist
        else:
            # get the rest of the information out of the contact
            # A lot is happening here! Think about this line.
            first = phonebook[last.lower()]['name'].split()[0]
            phone = phonebook[last.lower()]['phone']
            # ask what the user wants to change
            subchoice = raw_input("""
                Which would you like to change?
                \t1. Last name
                \t2. First name
                \t3. Phone number
                Enter the number of your choice. >> """)
            if subchoice == '1':
                # get the new last name
                new = raw_input("What is the new last name?")
                # create new, corrected contact under corrected key
                phonebook[new.lower()] = {'name': first + " " + new, 'phone': phone}
                # delete the old contact under the old last name
                del phonebook[last.lower()]
                # we're done
                break
            elif subchoice == '2':
                # get the new first name
                new = raw_input("What is the new first name?")
                # replace contact with corrected value
                phonebook[last.lower()] = {'name': new + " " + last, 'phone': phone}
                # we're done
                break
            elif subchoice == '3':
                # get the new phone number
                new = raw_input("What is the new phone number?")
                # replace contact with corrected value
                phonebook[last.lower()] = {'name': first + " " + last, 'phone': new}
                # we're done
                break
            else:
                print "That's not a choice!  Let's try this again.\n"


def delete():
    # keep track of whether or not we're done
    removed = False
    while not removed:
        # get the last name, put it in lowercase right away
        last = raw_input("What is the contact's last name?\n>> ").lower()
        # if no such contact exists,
        if last not in phonebook:
            # say so
            print "\nNo such contact exists?\n"
            # offer a second chance. If unwanted, we're done
            if raw_input("Try again? y/n >> ") != 'y':
                removed = True
        # if the contact does exist
        else:
            # confirm deletion
            question = "Are you sure you want to delete "
            question = question + phonebook[last]['name'] + ": "
            question = question + phonebook[last]['phone'] + "? y/n >> "
            # if confirmed, do it and say so.
            if raw_input(question) == 'y':
                del phonebook[last]
                print "Contact deleted."
            # confirmed or not, we're done.
            removed = True  # note how important the tabs are here.


def search():
    # another way to leave a function instantly is to `return` something.
    # this indicates to Python that the function has finished its computation.
    # Usually `return` actually returns an answer of some sort, but it doesn't
    # have to.
    
    while True:
        # get the last name, put it in lowercase right away
        last = raw_input("What is the contact's last name?\n>> ").lower()
        # if no such contact exists,
        if last not in phonebook:
            # say so
            print "\nNo such contact exists!\n"
            # offer a second chance. If unwanted, we're done
            if raw_input("Try again? y/n >> ") != 'y':
                return
        # if the contact does exist
        else:
            # print it out
            print phonebook[last]['name'] + ": " + phonebook[last]['phone']
            # we're done now.
            return


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
