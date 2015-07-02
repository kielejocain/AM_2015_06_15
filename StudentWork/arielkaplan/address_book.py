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
        self.id = None
        self.first_name = ""
        self.last_name = ""
        self.phone = ""
        self.email = ""

    def __str__(self):
        # print self.first_name + " " + self.last_name
        output = ""
        for attr, value in self.__dict__.iteritems():
            if value != "":
                output += str(attr) + ": " + str(value) + "\n"
        # output = "{id: " + str(self.id) + ", name: " + self.first_name + " " + self.last_name + "}"
        return output


class AddressBook(object):

    def __init__(self):
        self.people = {} # key is id, starting at 1
        self.last_id = 0

    def add(self, person):
        unique_id = self.last_id + 1
        # Add attr to Person
        person.id = unique_id
        # Add person to book
        self.people[unique_id] = person
        # increment id counter
        self.last_id += 1

    def read(self, id):
        return self.people[id]

    def update(self, id, parameter, new_input):
        update_person = self.people[id]
        update_person.parameter = new_input
        return self.people[id]

    def delete(self, id):
        delete_person = self.people[id]
        del delete_person

    def get_all(self):
        id_list = sorted(self.people.keys())
        output = ""
        for id in id_list:
            output += str(self.read(id)) + "\n"
        return output


# Using the classes the following test code should work
def test_book():
    book = AddressBook()
    person = Person()
    person.first_name = "Kevin"
    person.last_name = "Long"
    book.add(person)
    print(book.get_all())

test_book()