statement = raw_input("Please enter a statement to be reversed.\n> ")

print " ".join(statement.split()[::-1])

# or perhaps in more detail:
# words = statement.split()
# sdrow = words[::-1]
# output = " ".join(sdrow)
# print output 

# statement = raw_input("Please enter a statement to reverse.\n>> ")

# min = 0
# max = 0
# words = []

# for i in range(len(statement)):
	# if statement[i] == ' ':
		# max = i 
		# words.append(statement[min:max])
		# min = max + 1
	
# words.append(statement[min:])

# sdrow =words[::-1]

# output =''
# for word in sdrow[:-1]:
	# output += word
	# output += ' '
# output += sdrow[-1]

# print output 