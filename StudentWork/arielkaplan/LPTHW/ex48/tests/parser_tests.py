from nose.tools import *
from ex48 import parser

def test_subject():

	assert_equal(
		parser.parse_subject([("verb", "kill"), 
							  ("noun", "bear")]),
		('noun', 'player')
	)
	assert_equal(
		parser.parse_subject([("noun", "bear"), 
							  ("verb", "eat"), 
							  ("noun", "princess")]),
		('noun', 'bear')
	)
	assert_raises(
		parser.ParserError, # expected error
		parser.parse_subject, # function to run
		[("direction", "north"), ("verb", "go")] # arg for function
	)

def test_verb():
		
	assert_equal(
		# must start with verb
		parser.parse_verb([("verb", "kill"), 
						   ("noun", "bear")]),
		('verb', 'kill')
	)
	assert_raises(
		parser.ParserError, # expected error
		parser.parse_verb, # function to run
		[("direction", "north"), ("noun", "princess")] # arg for function
	)

def test_object():
	
	assert_equal(
		parser.parse_object([("noun", "bear")]),
		('noun', 'bear')
	)
	assert_equal(
		parser.parse_object([("noun", "princess"), 
							 ("error", "peach")]),
		('noun', 'princess')
	)
	assert_raises(
		parser.ParserError, # expected error
		parser.parse_object, # function to run
		[("verb", "go"), ("stop", "the")] # arg for function
	)


def test_sentence():

	phrase = parser.parse_sentence([('verb', 'kill'),
					   				('stop', 'the'),
					   				('noun', 'bear'),
					   				('error', 'now')])

	assert_equal(phrase.subject, 'player')
	assert_equal(phrase.verb, 'kill')
	assert_equal(phrase.object, 'bear')

	assert_raises(parser.ParserError, 
				  parser.parse_sentence, 
				  [('stop', 'the'), ('noun', 'bear')])

# redefine equality in Sentence class so you can test Sentence == Sentence
# or python will check memory id and say they are not equal
# alternative to testing sub/verb/obj separately as in above
def test_sentence_2():
	assert_equal(
		parser.parse_sentence([
			('verb', 'kill'),
			('noun', 'bear')
		]),
		parser.Sentence(
			('noun', 'player'),
			('verb', 'kill'),
			('noun', 'bear')
		)
	)
