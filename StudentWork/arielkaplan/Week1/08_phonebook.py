# Create a dictionary of dictionaries to hold your data.
phonebook = {
    'joecken': {'name': 'Kyle Joecken', 'phone': '503-555-1212'},
    'jones': {'name': 'Chris Jones', 'phone': '503-234-5678'}
    }


def add():
    # add an entry to your phonebook.
    last_name = raw_input("What is their last name? >> ")
    first_name = raw_input("What is their first name? >> ")
    phone = raw_input("What is their phone number? >> ")
    entry = {
        "name" : first_name + " " + last_name,
        "phone" : phone
        }
    phonebook[last_name.lower()] = entry
    print entry

def edit():
    # change an entry in your phonebook.  Use del if necessary!
    
    # if key there,
    # ask if change name or phone
    # save thing not changing for reuse
    # if name change, add new entry with new name and delete old entry



    searched = raw_input("What is the last name of the entry you'd like to edit? >> ")
    if searched.lower() in phonebook : 
        print phonebook[searched.lower()]["name"]
        print phonebook[searched.lower()]["phone"]
        print """
        Type 'name' to edit the name.
        Type 'phone' to edit the phone number.
        """
        to_edit = raw_input("What would you like to edit? >> ")
        
        if to_edit.lower() == "name" :
            last_name = raw_input("What is their updated last name? >> ")
            first_name = raw_input("What is their updated first name? >> ")
                phonebook[searched.lower()]["name"] : first_name + " " + last_name

        elif to_edit.lower() == "phone" :
            pass
            # phone = raw_input("What is their phone number? >> ")
        else : 
            print "That wasn't one of the choices."
            to_edit = raw_input("Please type 'first', 'last', or 'phone'.")
        
        new_entry = {
            "name" : first_name + " " + last_name,
            "phone" : phone
            }
        phonebook[last_name.lower()] = new_entry

        print "Here is the updated entry: "
        print phonebook[last_name.lower()]
        print new_entry

    else :
        print "That person is not in the phonebook."

def delete():
    # delete an entry from the phonebook if it exists.
    searched = raw_input("What is the last name of the person you'd like to delete? >> ")
    if searched.lower() in phonebook : 
        phonebook.pop(searched.lower())
        print "You've deleted the entry for " + searched
    else :
        print "That person is not in the phonebook."


def search():
    # find and print an entry if it exists.
    searched = raw_input("What is the last name of the person you're looking for? >> ")
    if searched.lower() in phonebook : 
        print phonebook[searched.lower()]
    else :
        print "That person is not in the phonebook."

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
