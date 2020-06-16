#  1. Create a Person class
#       Include properties/attributes for
#       a phone number, email address,
#       and separate first and last name fields

class Person(object):
    def __init__(self):
        self.first_name = ''
        self.last_name = ''
        self.number = ''
        self.email = ''
        self.id = None

    def __repr__(self):
        return "{id:" + str(self.id) + ", name: '" + self.first_name + " " + self.last_name + "'}"

#  2. Create an address book class
#       Initialize it with an empty dict of people
#       Add methods to create, read, update, and delete.
#       Each person added should be assigned a unique id.
#       THe ID should be a simple number that gets incremented.
#       e.g. 1, 2 , 3 etc

class AddressBook(object):
    def __init__(self):
        self.people = {}
        self.last_id = 1

    def add(self, person):
        person.id = self.last_id
        self.people[person.id] = person
        self.last_id += 1
        return person.id

    def get(self, id):
        if id in self.people:
            return self.people[id]
        else:
            return None

    def remove(self, person):
        if person.id in self.people:
            del self.people[person.id]

    def update(self, person):
        if person.id in self.people:
            self.people[person.id] = person
        return person

    def get_all(self):
        return self.people

# Using the classes the following test code should work
def test_book():
    book = AddressBook()
    person = Person()
    person.first_name = "Tree"
    person.last_name = "Casiano"
    person.email = "tree.pdx@gmail.com"
    id = book.add(person)
    print(book.get_all())
    p = book.get(id)
    p.first_name = "Theresa"
    book.update(p)
    print(book.get_all())

test_book()
