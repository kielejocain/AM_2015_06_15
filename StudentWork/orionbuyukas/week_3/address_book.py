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



    def __init__(self, first_name, last_name, phone_number, ID):
            self.first_name = first_name
            self.last_name = last_name
            self.phone_number = phone_number
            self.email_address = email_address
            self.ID = ID

            #or
    def __init__(self):
            self.first_name = "" #then assign using the .method. ie person.first_name = "orion"
            self.last_name = ""
            self.phone_number = ""
            self.email_address = ""
            self.id = ""




class AddressBook(object):

    def __init__(self):
        self.people = {}
        self.last_id = 1


    def read_contacts(self, id):
        if person.id in self.people:
            return self.people[id]
        return person # create new person


    def create_contact(self, person):
        person.id = last_id
        self.people[person.id] = person #person gives all fields for person get was probably used to find
        self.last_id += 1
        return person.id

    def update_contact(self):

    def delete_contact(self, person):
        if person.id in self.people:
            del self.people[person.id]







"""    def __init__(self, people, person):
        people = []

    def read_contact(self):
        contact_search = raw_input("Who are you looking for? ")
        if contact_search in people:
            print Person(contact_search)
        elif:
            make_new_contact = raw_input("That contact doesn't exist. Would you like to make a new contact? y/n").lower
            if make_new_contact == 'y':
                return create_contact()
            elif make_new_contact == 'n':
                return read_contact()"""
