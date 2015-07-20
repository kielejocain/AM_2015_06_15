# GIVEN THE FOLLOWING LIST OF LIST
test_data = [
    ["2014-06-01", "APPL", 100.11],
    ["2014-06-02", "APPL", 110.61],
    ["2014-06-03", "APPL", 120.22],
    ["2014-06-04", "APPL", 100.54],
    ["2014-06-01", "MSFT", 20.46],
    ["2014-06-02", "MSFT", 21.25],
    ["2014-06-03", "MSFT", 32.53],
    ["2014-06-04", "MSFT", 40.71],
]

# CREATE TWO NEW LISTS ONE FOR EACH STOCK TICKER SYMBOL e.g. APPL and MSFT

Apple = []
Microsoft = []

for name in test_data:
    name_abbreviation = name[1]
    if name_abbreviation == "APPL":
        Apple.append(name)
    elif name_abbreviation == "MSFT":
        Microsoft.append(name)
print Apple
print Microsoft

# Example Output to eliminate redundant data

def new_dictionary(test_data):
    # The next line defines the index position, in this case it is the name_abbreviation
    name_abbreviation = 1
    # The next line creates a new empty dictionary
    nameless_dictionary = {}
    for name in test_data:
        # The next line formats the code to show name: APPL or MSFT (then the data)
        column_value = name[name_abbreviation]
        # .keys method returns a list of all available keys in a dictionary
        keys = nameless_dictionary.keys()
        # The next line of code deals with all data that is not name, ie. APPL or MSFT
        if column_value not in keys:
            nameless_dictionary[column_value] = []
        list = nameless_dictionary[column_value]
        # The next line Removes the name, ie. the index position 1 from the new dictionary
        name.pop(name_abbreviation)
        # .append method passes an object into an existing list
        list.append(name)
        return nameless_dictionary

result = new_dictionary(test_data)
print result
print test_data


