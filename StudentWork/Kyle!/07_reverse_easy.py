# now we'll use built-in string methods to never have to talk about that again.

statement = raw_input("Please enter a smetantte to be reversed.\n> ")

print " ".join(statement.split()[::-1])

# or perhaps in more detail:
# words = statement.split()
# sdrow = words[::-1]
# output = " ".join(sdrow)
# print output
