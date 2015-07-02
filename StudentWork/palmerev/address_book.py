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
        self.id = None

    def __repr__(self):
        return "'{first} {last}'".format(first=self.first_name, last=self.last_name)

class AddressBook(object):
    id_number = 1
    def __init__(self):
        self.entries = {}

    def add(self, person):
        #person must be a Person object
        person.id = AddressBook.id_number
        self.entries[person.id] = person
        AddressBook.id_number += 1
        return person.id

    # "read"
    def search(self, id):
        #prints the contact info for id and returns True if found, else returns False
        if id in self.entries:
            entry = self.entries[id]
            print "Found entry:", entry
            print "phone:", entry.phone
            print "email:", entry.email
            return True
        else:
            print "Entry not found."
            return False

    def update(self, id, first_name=None, last_name=None, phone=None, email=None):
        person = self.entries[id]
        if first_name is not None:
            person.first_name = first_name
        if last_name is not None:
            person.last_name = last_name
        if phone is not None:
            person.phone = phone
        if email is not None:
            person.email = email

    def update_from_raw_input(self, person):
        if self.search(person):
            print "1) first name"
            print "2) last name"
            print "3) phone"
            print "4) email"
            option = 0
            while option not in [1, 2, 3, 4]:
                option = raw_input("Which item would you like to change (1 - 4)? ")
            if option == 1:
                new_first_name = raw_input("Enter a new first name: ")
                self.entries[person.id].first_name = new_first_name
            elif option == 2:
                new_last_name = raw_input("Enter a new last name: ")
                self.entries[person.id].last_name = new_last_name
            elif option == 3:
                new_phone = raw_input("Enter a new phone number: ")
                person.phone = new_phone
            else:
                new_email = raw_input("Enter a new email address: ")
                person = self.entries[target_name]["contact info"]
                person.email = new_email
                print "Phone for {first} {last} is {email}.".format(
                    first=person.first_name, last=person.last_name, email=person.email
                    )

    def delete_with_confirmation(self, person):
        if self.search(person.id):
            choice = None
            while choice.lower() not in ['y', 'n']:
                full_name = person.first_name + " " + person.last_name
                choice = raw_input("Are you sure you want to delete {name}? (y/n) ".format(full_name))
            if choice == 'y':
                print "Deleted {name}.".format(name=full_name)
                del self.entries[full_name]

    def delete(self, id):
        try:
            del self.entries[id]
        except KeyError:
            print "A person with id {x} doesn't exist.".format(x=id)

    def get_all(self):
        return str(self.entries)

def test_AddressBook():
    book = AddressBook()
    person1 = Person()
    person1.first_name = "Evan"
    person1.last_name = "Palmer"
    id1 = book.add(person1)
    person2 = Person()
    person2.first_name = "Kevin"
    person2.last_name = "Long"
    id2 = book.add(person2)
    print(book.get_all())
    book.update(id1, first_name="Python", last_name="is Awesome")
    book.update(id2, last_name="is Cool")
    print(book.get_all())
    book.search(1)
    book.search(2)
    book.search(3)
    book.delete(2)
    book.delete(3)
    print(book.get_all())

test_AddressBook()