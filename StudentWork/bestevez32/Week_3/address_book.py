#  1. Create a Person class
#       Include properties/attributes for
#       a phone number, email address,
#       and separate first and last name fields

class Person(object):
    def __init__(self):
        self.phone_number = ""
        self.email_address = ""
        self.name_first = ""
        self.name_last = ""

    def __repr__(self):
        return "{ id:" + str(self.id) + " name: %r " % self.name_first + self.name_last


#  2. Create an address book class
#       Initialize it with an empty dict of people
#       Add methods to create, read, update, and delete.
#       Each person added should be assigned a unique id.
#       THe ID should be a simple number that gets incremented.
#       e.g. 1, 2 , 3 etc

class AddressBook(object):
    def __init__(self):
        self.all_person = {}
        self.name_last = 1

    def create(self, person):
        person.id = self.name_last
        self.all_person[person.id] = person
        self.name_last += 1

    def read(self):
        if id in self.all_person:
            return self.all_person[id]
        else:
            return None

    def update(self, person):
        if self.name_last in self.all_person:
            self.all_person[person.id] = person
        return person

    def delete(self, person):
        if person.id in self.all_person:
            del self.all_person[person.id]
        else:
            print "No one home!"

    def get_all(self):
        return self.all_person





def test_book():
    book = AddressBook()
    person = Person()
    person.first_name = "Kevin"
    person.last_name = "Long"
    book.add(person)
    print(book.get_all())

