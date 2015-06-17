# this script should take in a sentence or statement from the user,
# then repeat that statement back with the words in reverse order.
# Do not reverse the words themselves!

statement = raw_input("Please enter a statment to reverse.\n>> ")

print " ".join( [x for x in reversed(statement.split(" "))] )

words = statement.split(" ")

rev = words[::-1]
new_string = ""
for word in rev:
    new_string += word + " "
new_string = new_string[:-1]
print new_string
