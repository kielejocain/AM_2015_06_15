# this script should take in a sentence or statement from the user,
# then repeat that statement back with the words in reverse order.
# Do not reverse the words themselves!


statement = raw_input("Please enter a staetment to reverse.\n>> ")

print " " .join(statement.split()[::-1])


# words = statement.split() splits into words
# sdrow = words[::-1] runs backwards

# output = " ".join(strow)
# print output
