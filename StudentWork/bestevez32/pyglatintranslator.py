pyg = 'ay'

original = raw_input('Enter a word to Pyg Latinize:')

if len(original) > 2 and original.isalpha():
	word = original.lower()
	first = word[0]
	new_word = word + first + pyg
	new_word = new_word[1:]
	print new_word
	
else:
	print 'Try entering a word that I can work with'
