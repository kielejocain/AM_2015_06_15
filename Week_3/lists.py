# create a new empty list
me = []
# another way to do the same
me = list()

# add two new items to the list
me.append("Kevin")
me.append("Long")

# we often see this done in short hand all at once e.g.:
me = ["Kevin", "Long"]

# print first name which is the first item
# the first item is at list index zero
print(me[0])

# print last name which is the second item
# the second item is at list index 1
print(me[1])

# print full name
print(me[0] + " " + me[1])

# We often define constants to make this more clear
# print full name using constants
FIRST_NAME = 0
LAST_NAME = 1
print(me[FIRST_NAME] + " " + me[LAST_NAME])
