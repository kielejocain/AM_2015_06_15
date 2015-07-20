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

# Using the classes the following test code should work
# def test_book():
#     book = AddressBook()
#     person = Person()
#     person.first_name = "Kevin"
#     person.last_name = "Long"
#     book.add(person)
#     print(book.get_all())
# test_book()

class AddressBook():
    def __init__(self):
        self.people = {}
        self.last_id = 1

    def add(self, person):
        # function is called by last name
        person.id = self.last_id
        # list [] gets created because it is mutable
        # self.people[person.id] creates a hierarchy all person
        # is people but not vice versa
        self.people[person.id] = person
        # This adds + 1 to the last record created
        self.last_id +=1

    def get_all(self):
        return self.people


class Person(object):
    def __init__(self):
        self.first_name = ""
        self.last_name = ""

    def __repr__(self):
        return "{id:" + str(self.id) + ", name: '" + self.first_name + " " + self.last_name + "'}"


test_book()
