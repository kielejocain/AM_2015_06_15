# this script should take in a sentence or statement from the user,
# then repeat that statement back with the words in reverse order.
# Do not reverse the words themselves!

statement = raw_input("Please enter a statement to reverse.\n>> ")
#value =list[start:end]
#print value[end:start]

min = 0
max = 0
words = []

for i in range(len(statement)):
	if statement[i] == ' ':
		max = i 
		words.append(statement[min:max])
		min = max + 1
	
words.append(statement[min:])

sdrow =words[::-1]

output =''
for word in sdrow[:-1]:
	output += word
	output += ' '
output += sdrow[-1]

print output 

#print statement 

	
	

# The statement below will reverse the statement one letter at a time
#print statement, "in reverse is", statement[::-1]


#for c in statement:
	#do something
	
# Statement is A and B, to print B and A 