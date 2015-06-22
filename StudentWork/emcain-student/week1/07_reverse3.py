# this script should take in a sentence or statement from the user,
# then repeat that statement back with the words in reverse order.
# Do not reverse the words themselves!

statement = raw_input("Please enter a statment to reverse.\n>> ")

words_list = []
the_word = ""

reverse_statement = ""

for c in statement:
	#test if the character is a space 
	if c == ' ':
		#if it is a space, add the temporary string variable to a list of words
		words_list.append(the_word)
		the_word = ""
	#if it is not a space add it to the temporary string variable
	else:
		the_word = the_word + c
words_list.append(the_word)
		
n = len(words_list)
rev_words_list = []
i = 0

while n > i:
	i += 1
	rev_words_list.append(words_list[-i])


for word in rev_words_list:
	reverse_statement += word
	reverse_statement += " "
	
print reverse_statement