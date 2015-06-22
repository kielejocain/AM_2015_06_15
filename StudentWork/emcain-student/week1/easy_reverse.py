statement = raw_input("Please enter a thing to be reversed.")

print " ".join(statement.split()[::-1]) #applying the join method to the string " " taking the argument statement.split

#or
words = statement.split()
sdrow = words[::-1]
output = " ".join(sdrow)
print output 

#objects -- nouns
#methods -- verbs
#attributes -- adjectives

#object.method