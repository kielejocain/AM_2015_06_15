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

    def __repr__(self):
        # print self.first_name + " " + self.last_name
        # output = ""
        # for attr, value in self.__dict__.iteritems():
        #     if value != "":
        #         output += str(attr) + ": " + str(value) + "\n"
        output = "{id: " + str(self.id) + ", name: " + self.first_name + " " + self.last_name + "}"
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

    def read(self, person):
        return self.people[person.id]

    def get(self, id):
        print id
        return self.people[id]

    def update(self, person):
        if person.id in self.people.keys():
            self.people[person.id] = person
        return person

    def delete(self, person):
        if person.id in self.people.keys():
            del self.people[person.id]

    def get_all(self):
        id_list = sorted(self.people.keys())
        output = {}
        for id in id_list:
            current_person = self.people[id]
            output[id] = (self.read(current_person))
        return output

    def find_all_matches(self, parameter, searched_term):
        matches = []
        searched_term = searched_term.lower()
        # or key, value in dict.items()
        for person in self.people.values():
            if person.__dict__[parameter].lower() == searched_term:
                matches.append(person)
        return matches

    def fuzzy_find_all_matches(self, parameter, searched_term):
        matches = []
        searched_term = searched_term.lower()
        for person in self.people.values():
            possible_match = person.__dict__[parameter].lower()
            if possible_match.find(searched_term) != -1:
                matches.append(person)
        return matches



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
    person.first_name = "Kayla"
    person.last_name = "Smith"
    id3 = book.add(person)

    print("\nALL BEFORE Nemo change:")

    for i, item in book.get_all().items():
        print(item)

    # retrieve person by id
    p = book.get(1)

    # change persons name
    p.first_name = "Nemo"

    # update person to change name
    book.update(p)

    print("\nALL after change to Nemo:")
    for i, item in book.get_all().items():
        print(item.id, item.first_name, item.last_name)

    print("\nFIND last_name == 'Long':")
    for item in book.find_all_matches("last_name", "Long"):
        print(item.id, item.first_name, item.last_name)

    print("\nFUZZY FIND first_name like '%a%' :")
    for item in book.fuzzy_find_all_matches("first_name", "a"):
        print(item.id, item.first_name, item.last_name)


test_book()