#  1. Create a Person class
#       Include properties/attributes for
#       a phone number, email address,
#       and separate first and last name fields

#  2. Create an address book class
#       Initialize it with an empty list of people
#       Add methods to create, read, update, and delete.
#       Each person added should be assigned a unique id.
#       THe ID should be a simple number that gets incremented.
#       e.g. 1, 2 , 3 etc

class Person(object):
    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.phone = ""
        self.email = ""

class AddressBook(object):
    id_number = 1
    def __init__(self):
        #each entry inserted by add() will be a dict with two keys.
        self.entries = {}

    def add(self, person):
        #person must be a Person object
        full_name = " ".join([person.first_name, person.last_name])
        if full_name in self.entries:
            print "There is already an entry with that name. Please choose a different name."
            return
        self.entries[full_name] = {"id": AddressBook.id_number, "contact info": person}
        AddressBook.id_number += 1
    # "read"
    def search(self, target_name):
        #prints the contact info for target_name and returns True if found, else returns False
        if target_name in self.entries:
            entry = self.entries[target_name]
            print "Found entry: "
            print entry["contact info"].first_name, " ", entry["contact info"].last_name
            print entry["contact info"].phone
            print entry["contact info"].email
            return True
        else:
            print "Entry not found."
            return False

    def update(self, target_name):
        if self.search(target_name):
            print "1) first name"
            print "2) last name"
            print "3) phone"
            print "4) email"
            option = 0
            while option not in [1, 2, 3, 4]:
                option = raw_input("Which item would you like to change (1 - 4)? ")
            if option == 1:
                old_person = self.entries[target_name]["contact info"]
                new_first_name = raw_input("Enter a new first name: ")
                new_full_name = " ".join(new_first_name, old_person.last_name)
                while new_full_name in self.entries.keys():
                    new_first_name = raw_input(
                        "{name} already exists. Please choose a different first name: ".format(name=new_full_name)
                    )
                    new_full_name = " ".join([old_person.first_name, new_last_name])
                new_person = Person()
                new_person.first_name = new_first_name
                new_person.last_name = old_person.last_name
                new_person.phone = old_person.phone
                new_person.email = old_person.email
                self.add(new_person)
                del self.entries[target_name]
            elif option == 2:
                old_person = self.entries[target_name]["contact info"]
                new_last_name = raw_input("Enter a new last name: ")
                new_full_name = " ".join([old_person.first_name, new_last_name])
                while new_full_name in self.entries.keys():
                    new_last_name = raw_input(
                        "{name} already exists. Please choose a different last name: ".format(name=new_full_name)
                    )
                    new_full_name = " ".join([old_person.first_name, new_last_name])
                new_person = Person()
                new_person.first_name = old_person.first_name
                new_person.last_name = new_last_name
                new_person.phone = old_person.phone
                new_person.email = old_person.email
                self.add(new_person)
                del self.entries[target_name]
            elif option == 3:
                new_phone = raw_input("Enter a new phone number: ")
                person = self.entries[target_name]["contact info"]
                person.phone = new_phone
                print "Phone for {first} {last} is {phone}.".format(
                    first=person.first_name, last=person.last_name, phone=person.phone
                    )
            else:
                new_email = raw_input("Enter a new email address: ")
                person = self.entries[target_name]["contact info"]
                person.email = new_email
                print "Phone for {first} {last} is {email}.".format(
                    first=person.first_name, last=person.last_name, email=person.email
                    )
    def delete(self, target_name):
        if self.search(target_name):
            choice = None
            while choice.lower() not in ['y', 'n']:
                choice = raw_input("Are you sure you want to delete {name}? (y/n) ".format(name=target_name))
            if choice == 'y':
                print "Deleted {name}.".format(name=target_name)
                del self.entries[target_name]

def test_AddressBook():
    book = AddressBook()
    person = Person()
    person.first_name = "Kevin"
    person.last_name = "Long"
    book.add(person)

test_AddressBook()