# Create a dictionary of dictionaries to hold your data.
phonebook = {
    'joecken': {'name': 'Kyle Joecken', 'phone': '503-555-1212'},
    'jones': {'name': 'Chris Jones', 'phone': '503-234-5678'}
    }


def add():
    # add an entry to your phonebook.
    last_name = raw_input("Last name?")
    first_name = raw_input("first name?")
    phone = raw_input("phone number?")
    entry = {
		'name': first_name + " " + last_name,
		'phone': phone
    }
    phonebook[last_name.lower()] = entry
    print entry['name']
    


def edit():
    # change an entry in your phonebook.  Use del if necessary!
    #use .update then pass in a dict of the updated info
    contact = raw_input("Who do you want to edit?")
    phonebook.get(contact)
    print phonebook[contact]
    choice = raw_input("What would you like to change? name or phone?")
	if choice == 'name':
		new_name = raw_input("Please enter the new name")
		contact['name'] = new_name		
    


def delete():
	contact = raw_input("Enter the last name of a person you want to delete")
	contact.lower()
	del phonebook[contact]
	
    # delete an entry from the phonebook if it exists.
    


def search():
    # find and print an entry if it exists.
    contact = raw_input("Who are you looking for?")
    print phonebook.get(contact)
    


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
