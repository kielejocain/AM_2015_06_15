# Create a dictionary of dictionaries to hold your data.
phonebook = {
    'joecken': {'name': 'Kyle Joecken', 'phone': '503-555-1212'},
    'jones': {'name': 'Chris Jones', 'phone': '503-234-5678'}
    }


def add():
    # add an entry to your phonebook.
	last_name = raw_input("What's the last name of the contact? ")
    first_name = raw_input("What's the first name of the contact? ")
    phone = raw_input("What's the phone number? ")
    entry = {
	'name': first_name + " " + last_name,
	}
    phonebook[last_name.lower()] = entry
    print entry['name']

def edit():
    # change an entry in your phonebook.  Use del if necessary!
    pass


def delete():
    # delete an entry from the phonebook if it exists.
	last_name = ("What contact would you like to delete? ")
    if name in phonebook:
        del entry ['name']
    else:
        print name, " not found"


def search():
    # find and print an entry if it exists.
    pass


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
