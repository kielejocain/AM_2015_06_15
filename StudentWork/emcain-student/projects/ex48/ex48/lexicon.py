#for each word type: 
# create some type, word tuples
# add them to a list of tuples 
# have this be generalizable so i can use a text file later. use a for loop. 


word_tuples = []

for tup in [('direction', 'north'),
			  ('direction', 'south'),
			  ('direction', 'east'),
			  ('verb', 'go'),
			  ('verb', 'kill'),
			  ('verb', 'eat'),
			  ('stop', 'the'),
              ('stop', 'in'),
              ('stop', 'of'),
			  ('noun', 'bear'),
			  ('noun', 'princess')
			  ]:
	
	word_tuples.append(tup)
	
for part in ['nouns', 'pronouns', 'prepositions', 'verbs']:
	the_file = open("ex48/" + part + ".txt")
	# print 'doing stuff with', part
	the_words = []
	
	for line in the_file:
		# print 'processing line', line
		line_words = line.split()
		for x in [1, 3, 5]:
			try:
				# print "printing word", x
				the_words.append(line_words[x])
				# print line_words[x]
			except IndexError:
				pass
	
	part_of_speech = ""
	if part == 'nouns' or  part == 'pronoun':
		part_of_speech = "noun"
	elif part == 'prepositions':
		part_of_speech = 'direction'
	else:
		part_of_speech = 'verb'
	
	for word in the_words:
		# print "appending to word_tuples", part_of_speech, word 
		word_tuples.append((part_of_speech, word))
		
	
	



def is_int(input):
	try:
		int(input)
		return True
	except ValueError:
		return False

def scan(input):
	#split the input string
	inputs = input.split()
	#loop over it somehow doing the following

	output = []
	for indiv in inputs: 
		for (type, word) in word_tuples:
			if word == indiv:
				output.append((type, word))
				break
		else: # means "no break" when used on loops 
			if is_int(indiv):
				output.append(('number', int(indiv)))
			else:
				output.append(('error', indiv)) # shouldn't happen if the inner for loop added it. 
	return output

