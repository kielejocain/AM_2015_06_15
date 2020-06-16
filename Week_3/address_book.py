#  1. Create a Person class
#       Include properties/attributes for
#       a phone number, email address,
#       and separate first and last name fields

#  2. Create an address book class
#       Initialize it with an empty dict of people
#       Add methods to create, read, update, and delete.
#       Each person added should be assigned a unique id.
#       THe ID should be a simple number that gets incremented.
#       e.g. 1, 2 , 3 etc

# Using the classes the following test code should work
def test_book():
    book = AddressBook()
    person = Person()
    person.first_name = "Kevin"
    person.last_name = "Long"
    book.add(person)
    print(book.get_all())


test_book()
