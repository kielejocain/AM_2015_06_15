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

class AddressBook():
    def __init__(self):
        self.people = {}
        self.last_id = 1

    def add(self, person):
        person.id = self.last_id
        self.people[person.id] = person
        self.last_id += 1
        return person.id

    def update(self, person):
        if person.id in self.people:
            self.people[person.id] = person
        return person

    def get(self, id):
        if id in self.people:
            return self.people[id]
        else:
            return None

    def remove(self, person):
        if person.id in self.people:
            del self.people[person.id]

    def get_all(self):
        return self.people

    def find_all_matches(self, property_name, property_value):
        output = []
        for i, p in self.people.items():
            if p.__dict__[property_name] == property_value:
                output.append(p)
        return output


class Person(object):
    def __init__(self):
        self.id = None
        self.first_name = ""
        self.last_name = ""

    def __repr__(self):
        return "{id:" + str(self.id) + ", name: '" + self.first_name + " " + self.last_name + "'}"


# Using the classes the following test code should work
def test_book():
    book = AddressBook()

    person = Person()
    person.first_name = "Kevin"
    person.last_name = "Long"
    id = book.add(person)

    person = Person()
    person.first_name = "Kay"
    person.last_name = "Long"
    id2 = book.add(person)

    person = Person()
    person.first_name = "John"
    person.last_name = "Smith"
    id3 = book.add(person)

    for i, item in book.get_all().items():
        print(item)

    # reteive person by id
    p = book.get(id)

    # change persons name
    p.first_name = "Nemo"

    # update person to change name
    book.update(p)

    for i, item in book.get_all().items():
        print(item.id)
        print(item.first_name)
        print(item.last_name)

    for item in book.find_all_matches("last_name", "Long"):
        print(item.id, item.first_name, item.last_name)


test_book()
