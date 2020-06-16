# this script should take in a sentence or statement from the user,
# then repeat that statement back with the words in reverse order.
# Do not reverse the words themselves!

statement = raw_input("Please enter a statment to reverse.\n>> ")

# Short version

print " ".join(statement.split()[::-1])
# or in more detail:
words = statement.split()
sdrow = words[::-1]
output = " ".join(sdrow)
print output

# Long version

words = []
start = 0

for i in range(len(statement)) :
	if statement[i] == " " : 
		end = i
		words.append(statement[start:end])
		start = i + 1
		print words
# add last word 
words.append(statement[start:])
print words

reverse_statement = ""

for word in words[::-1] :
	reverse_statement += word
	if word != words[0] :
		reverse_statement += " "
print reverse_statement


# for char in statement[:] :
# 	if char == " " : 
# 		i = statement.index(char)
# 		print i
# 		words.append(statement[start:i])
# 		# statement = statement[i:]
# 		start = i
# words.append(statement[start:])
# print words
