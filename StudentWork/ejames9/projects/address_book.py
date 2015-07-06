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

class Person(object):
    def __init__(self, phone_number, email_address, first_name, last_name):
        self.phone_number = phone_number
        self.email_address = email_address
        self.first_name = first_name
        self.last_name = last_name

class AddressBook():
    def __init__(self, peeps):
        self.peeps = []

    def add_entry(self,):