# this script should take in a sentence or statement from the user,
# then repeat that statement back with the words in reverse order.
# Do not reverse the words themselves!

statement = raw_input("Please enter a statment to reverse.\n>> ")

words_list = statement.split()
words_list.reverse()

reverse_statement = ""

for word in words_list:
	reverse_statement += word
	reverse_statement += " "
	
print reverse_statement