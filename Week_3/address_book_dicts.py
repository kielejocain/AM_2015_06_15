__author__ = 'Emily'

class Person(object):

    def __init__(self, first_name, last_name, phone, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = str(phone)
        self.email = email

    def __repr__(self):
        return "Name: " + self.first_name + " " + self.last_name + " | Phone: " + self.phone + " | Email: " + self.email
        # to get everything after and including the first pipe symbol: person.string(find("|":))

class AddressBook(object):

    def __init__(self):
        self.people = {}

    def add_person(self, first_name, last_name, phone, email):
        self.people[first_name.lower() + "_" + last_name.lower()] = (Person(first_name, last_name, phone, email))

    def show_all_entries(self):
        output = ""
        for item in self.people.keys():
            output += str(self.people[item]) + "\n"
        if output == "":
            output = "There is no one in the address book."
        return output

    def search_people(self, info):
        output_dict = {}
        for entry in self.people.keys(): # entry is a key.
            for item in [self.people[entry].first_name,
                         self.people[entry].last_name,
                         self.people[entry].phone,
                         self.people[entry].email]:
                if info.lower() in item.lower():
                    output_dict[entry] = self.people[entry] #  in output_dict, create a key that is the old key
                                                            #  with a value that is the old value.
        return output_dict

    def remove_person(self, key):
        del self.people[key]
        print key, "removed from address book."


    def update_people(self, person, item_name, new_entry):
        lower_item = item_name.lower()
        if lower_item == "name" or lower_item == "full name":
            names = new_entry.split()
            person.first_name = names[0]
            person.last_name = names[-1]
        elif "first" in lower_item:
            person.first_name = new_entry
        elif "last" in lower_item:
            person.last_name = new_entry
        elif "phone" in lower_item:
            person.phone = new_entry
        elif "email" in lower_item or "e-mail" in lower_item or "e mail" in lower_item: # change to regex
            person.email = new_entry
        else:
            raise ValueError(
                "item_name must contain name (full name), first (first name), last (last name), phone, or email"
            )

book = AddressBook()

def search_display():
    term = str(raw_input("Please enter a name, phone number, or email address to search for:  "))
    print "Please wait..."
    results = book.search_people(term)
    print "These are the people whose info contains", term + ":\n"
    for item in results.keys():
        print item, ":", book.people[item]
    return results

def funct_search():
    while True:
        results = search_display()
        if len(results) == 0:
            print "Sorry, there is no one in the dictionary matching your search."
        else:
            break

    print "Whose entry do you want to delete?"
    while True:
        try:
            sel = raw_input("Enter person's ID from search results >> ")
            print "keys:", results.keys()
            if sel not in results.keys():
                raise ValueError
            break
        except (TypeError, ValueError):
            print "Please enter ID in form firstname_lastname."
    return sel


#----------
menu = {}
menu['1']="View all Entries"
menu['2']="Add Entry"
menu['3']="Search for Entry"
menu['4']="Edit Entry"
menu['5']="Delete Entry"
menu['6']="Exit"
while True:
    options=menu.keys()
    options.sort()
    print ("\nPlease select one of the following options:")
    for entry in options:
        print "\t", entry, menu[entry]
    selection=raw_input(">>  ")

    if selection =='1':
        print book.show_all_entries()

    elif selection == '2':
        # add_person(self, first_name, last_name, phone, email):
        print "Please enter the new person's information."

        first = raw_input("First Name:  ")
        last = raw_input("Last Name:  ")
        phone = raw_input("Phone Number:  ")
        email = raw_input("Email address:  ")

        book.add_person(first, last, phone, email)
        print "Added", first, last, "to the phone book."

    elif selection == '3':
        search_display()

    elif selection == '4':
        results = search_display()
        if results is None:
            break
        print "Whose entry do you want to edit?"
        while True:
            try:
                sel = raw_input("Enter person's ID from search results >> ")
                if sel not in results.keys():
                    raise ValueError
                break
            except (TypeError, ValueError):
                print "Please enter ID in form firstname_lastname."

        the_person = results[sel]

        print "Editing entry for", the_person.first_name, the_person.last_name

        while True:
            try:
                field = raw_input("Which field do you want to edit?")
                new = raw_input("What do you want to change the person's " + field + " to?")
                book.update_people(the_person, field, new)
                print "Updated" + the_person.first_name, the_person.last_name + "'s", field, "to", new
                break
            except (ValueError, NameError):
                print "Please make sure you enter a valid field, such as name, first, last, email or phone. "

    elif selection == '5':
        # results = search_display()
        # if len(results) == 0:
        #     "Sorry, there is no one in the dictionary matching your search."
        #     continue
        # print "Whose entry do you want to delete?"
        # while True:
        #     try:
        #         sel = raw_input("Enter person's ID from search results >> ")
        #         print "keys:", results.keys()
        #         if sel not in results.keys():
        #             raise ValueError
        #         break
        #     except (TypeError, ValueError):
        #         print "Please enter ID in form firstname_lastname."

        #  the_person = results[sel] # code up to here is copied from item 4. could make a function.

        sel = funct_search()

        book.remove_person(sel)

        print "Removed entry for", sel, "from the phone book. "

    else:
      print "Please type the number of the option you wish to select, then press 'Enter.'"