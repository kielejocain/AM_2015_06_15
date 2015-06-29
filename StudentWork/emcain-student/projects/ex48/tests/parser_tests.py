from nose.tools import *
from ex48 import lexicon
from ex48 import parser

def test_basic_sentence():
	tester = lexicon.scan("woman go outside")
	print tester
	assert_equal(str(parser.parse_sentence(tester)), "subject: woman     verb: go     object: outside")
	
# def test_complex_sentence():
	
# def test_no_subject():
	# pass
	
# def test_no_verb():
	# pass
	
# def test_empty_string():
	# pass
	
# def test_extra_words():
	# pass

# def test_with_numbers():
	# pass
	
# def test_junk_string():

