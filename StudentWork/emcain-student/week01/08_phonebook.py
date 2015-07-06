# Create a dictionary of dictionaries to hold your data.
phonebook = {
	#This is a dictionary entry with a key of joecken and a value of a subdicitonary containing 'name' and 'phone' entries
    'joecken': {'name': 'Kyle Joecken', 'phone': '503-555-1212'}, 
    'jones': {'name': 'Chris Jones', 'phone': '503-234-5678'}
    }


def add():
	print("Please enter info for the new contact.")
	last_name = raw_input("Last name: >> ")
	first_name = raw_input("First name: >> ")
	phone = raw_input("Phone Number: >> ")
	entry = {
		'name': first_name + " " + last_name,
		'phone': phone  
		}
	phonebook[last_name.lower()] = entry 
	print entry['name'] + " has been added to the phone book."


def edit():
    # change an entry in your phonebook.  Use del if necessary!
    pass


def delete():
    # delete an entry from the phonebook if it exists.
	to_delete = raw_input("Please enter the last name of the person whose info you wish to delete. >> ")
	the_entry = search(to_delete)
	if the_entry is not None: 
		print "Are you sure you wish to delete " + the_entry['name'] + "'s contact information? "
		answer = raw_input("Enter y/n >> ")
		if answer == "y":
			# delete the entry
			del phonebook[to_delete]
			print "Entry has been deleted."
		else:
			print "Entry not deleted."
		#need to add error handling to this 
	else: 
		print to_delete + " does not exist, so nothing was deleted."
	
	

def search(search_term=None): #sets default search term to None
	if search_term is None:
		search_term = raw_input("Please enter person's last name. >> ")
	if search_term.lower() in phonebook:
		entry = phonebook[search_term.lower()]
		print entry['name'] + " has phone number " + entry['phone']
		return entry
	else:
		print "Sorry, that is not a valid last name."

	#to do: allow for search on partial match; allow for search on other terms (first name, phone number)
	
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
