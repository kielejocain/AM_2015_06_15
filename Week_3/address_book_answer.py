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

    def fuzzy_find_all_matches(self, property_name, sought):
        output = []
        for i, p in self.people.items():
            # if property_value in p.__dict__[property_name]:
            property_value = p.__dict__[property_name].upper()
            sought = sought.upper()
            found = (property_value.find(sought) != -1)
            if found:
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
    person.first_name = "Kayla"
    person.last_name = "Smith"
    id3 = book.add(person)

    print("\nALL BEFORE Nemo change:")

    for i, item in book.get_all().items():
        print(item)

    # reteive person by id
    p = book.get(id)

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
