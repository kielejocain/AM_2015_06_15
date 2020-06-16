# this script should take in a sentence or statement from the user,
# then repeat that statement back with the words in reverse order.
# Do not reverse the words themselves!

statement = raw_input("Please enter a statement to reverse.\n>> ")

statement = statement.split()

i = len(statement)

while i > 0:
	word = statement.pop()
	print word,
	i -= 1

min = 0
max = 0
words = []
# This doesn't run if the statement is still a list. 
#Comment out the code above.
for i in range(len(statement)):
	if statement[i] == " ":
		max = i
		words.append(statement[min:max])
		min = i + 1

words.append(statement[min:])
reverse = words[::-1]

output = ""
for word in reverse:
	output += word
	output += " "
	
	
reverse_statement = " ".join(reverse)
print reverse_statement



#One line of code to do all the things!
#print "".join(statement.split()[::-1])
	

	
	
