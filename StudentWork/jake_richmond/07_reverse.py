# this script should take in a sentence or statement from the user,
# then repeat that statement back with the words in reverse order.
# Do not reverse the words themselves!

statement = raw_input("Please enter a statement to reverse.\n>> ")
min = 0 
max = 0
words = []

# statement is hello world

for i in range(len(statement)):
	if statement[i] == ' ':
		max = i
		words.append(statement[min:max])
		min = max + 1
		
words.append(statement[min:])

sdrow = words[::-1]

output = ""
for word in sdrow[:-1]:
	output += word
	output += " "
output += sdrow[-1]

print output