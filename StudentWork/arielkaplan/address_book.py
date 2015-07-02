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

    def __init__(self, first_name, last_name, phone, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.id = None

    def __str__(self):
        return ("Name: " + self.first_name + " " + self.last_name +
                "\nPhone: " + self.phone +
                "\nEmail: " + self.email
        )

class AddressBook(object):

    def __init__(self):
        self.people = {} # list of people objects, index is id
        self.ids = sorted(self.people.keys())

    def create(self, first_name, last_name, phone, email):
        new_person = Person(first_name, last_name, phone, email)
        if len(self.ids) == 0:
            unique_id = 1
        else:
            # find last element of sorted id # and add one
            unique_id = self.ids[-1] + 1
        new_person.id = unique_id
        self.people[unique_id] = new_person
        print ("You have added " + new_person.first_name + " " + new_person.last_name +
               " to your address book.")
        print new_person

    def read(self, parameter): # for now, assume parameter is id
        # for person in self.people:
        #     try:
        #         parameter.lower()
        #
        #     except:
        #         (person.first_name.lower() == parameter.lower()) or
        #         (person.last_name.lower() == parameter.lower()) or
        #         (person.phone == parameter) or
        #         (person.email.lower() == parameter.lower()) or
        #         (person.id == parameter)
        #         return person
        return self.people[id]

    def update(self, id, parameter):
        update_person = self.people[id]
        update_person.parameter = raw_input("Input new " + parameter + ": ")
        return self.people[id]

    def delete(self, parameter): # for now, assume parameter is id
        id = parameter
        delete_person = self.people[id]
        print delete_person
        confirm = raw_input("Are you sure you want to delete this person? y/n ")
        if confirm.lower() == 'y':
            del delete_person
            print "Entry deleted."
        else:
            print "Delete aborted."

    def find_id(self, parameter):
        # check if
        if parameter in self.people.keys():
            return parameter


test_first = "Jane"
test_last = "Doe"
test_phone = "555-123-4567"
test_email = "jane@example.com"
update_first = "John"

my_addresses = AddressBook()
my_addresses.create(test_first, test_last, test_phone, test_email)
my_addresses.update(1, "first_name")


