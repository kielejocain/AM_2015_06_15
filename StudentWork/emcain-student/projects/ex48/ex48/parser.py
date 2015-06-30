from lexicon import * 

class ParserError(Exception):
	pass
	
class Sentence(object):

	def __init__(self, subject, verb, obj):
		# remember we take ('noun', 'princess') tuples and convert them
		self.subject = subject[1]
		self.verb = verb[1]
		self.obj = obj[1]
		
	def __str__(self):
		return "subject: " + self.subject + "     verb: " + self.verb + "     object: " + self.obj
		
		
# looks at a list of words and return what type of word it (what)? is
def peek(word_list):
	if word_list:
		word = word_list[0]
		return word[0]
	else: 
		return None
	
#confirms the expected word is the right type (how?), takes it off the list, and returns the word. 	
def match(word_list, expecting):
	if word_list:
		word = word_list.pop(0)
		
		if word[0] == expecting: # ah I see, word[0] is the word's type while word[1] is the word itself
			return word
		else: 
			return None
	else:
		return None
		
def skip(word_list, word_type): #skip all words of this type in the word_list
	while peek(word_list) == word_type:
		match(word_list, word_type)
		
def parse_verb(word_list):
	skip(word_list, 'stop')
	next_word = peek(word_list)
	
	if next_word == 'verb':
		return match(word_list, 'verb')
	else:
		raise ParserError("Expected a verb next.")
		
def parse_object(word_list):
	skip(word_list, 'stop')
	next_word = peek(word_list)
	
	if next_word == 'noun':
		return match(word_list, 'noun')
	elif next_word == 'direction':
		return match(word_list, 'direction')
	else:
		raise ParserError("Expected a noun or direction next.")
		
def parse_subject(word_list):
	skip(word_list, 'stop')
	next_word = peek(word_list)
	
	if next_word == 'noun':
		return match(word_list, 'noun')
	elif next_word == 'verb':
		return ('noun', 'player')
	else:
		raise ParserError("Expected a verb next.")
		
def parse_sentence(word_list):
	subj = parse_subject(word_list)
	verb = parse_verb(word_list)
	obj = parse_object(word_list)
	
	return Sentence(subj, verb, obj)


