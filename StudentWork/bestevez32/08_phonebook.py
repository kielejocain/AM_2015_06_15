# Create a dictionary of dictionaries to hold your data.
phonebook = {
    'joecken': {'name': 'Kyle Joecken', 'phone': '503-555-1212'},
    'jones': {'name': 'Chris Jones', 'phone': '503-234-5678'},
	'estevez': {'name':'Brandon Estevez', 'phone': '503-555-5555'}
			}


def add():
    # add an entry to your phonebook.
	last_name = raw_input("What is the last name of the contact?>>")
	first_name = raw_input("What is the first name of the contact?>>")
	phone = raw_input("What is the phone number of the contact?>>")
	entry = {
		'name': first_name + " " + last_name,
		'phone': phone
		}
	pass


def edit():
    # change an entry in your phonebook.  Use del if necessary!
	last_name = raw_input("What is the name of the contact to edit?>>")
	del phonebook [last_name.lower()]
	last_name = raw_input("What is the new last name of the contact?>>")
	first_name = raw_input("What is the first name of the contact?>>")
	phone = raw_input("What is the phone number of the contact?>>")
	entry = {
		'name': first_name + " " + last_name,
		'phone': phone
		}
	



def delete():
    # delete an entry from the phonebook if it exists.
    # Brandon Entry: print ("What is the %r of the contact to delete?") % last_name 
	last_name = raw_input("What is the last name of contact to delete?>>")
	del phonebook [last_name.lower()] 
	print phonebook
	


def search():
    # find and print an entry if it exists.
	last_name = raw_input("What is the last name of the contact?>>")
	if last_name in phonebook: 
		print "This contact is in this phone book."
	else:
		print "This contact is not in this phone book, choose option 2 to add a contact."
	
 


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
