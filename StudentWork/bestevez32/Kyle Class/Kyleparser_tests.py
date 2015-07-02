from nose.tools import *
from ex48 import parser

## to test errors that SHOULD be raised, we use assert_raises.
## the arguments are:
##      1) the errorType to be raised (ParserError)
##      2) the function call that rases the error (note no parentheses)
##      3) the arguments to be passed into the function in order.

# first, we test the subject parser
def test_subject():
    # 'go north' starts with a verb: implied subject == 'player'
    assert_equal(
        parser.parse_subject([
            ('verb', 'go'),
            ('direction', 'north')
        ]),
        ('noun', 'player')
    )
    # 'bear eat honey': subject is 'bear'
    assert_equal(
        parser.parse_subject([
            ('noun', 'bear'),
            ('verb', 'eat'),
            ('noun', 'honey')
        ]),
        ('noun', 'bear')
    )
    # 'back north': ParserError
    assert_raises(
        parser.ParserError,        # errorType
        parser.parse_subject,      # function expected to raise error
        [('direction', 'back'), ('direction', 'north')] # args
    )

# next, the verb parser
def test_verb():
    # 'go north': verb is 'go'
    assert_equal(
        parser.parse_verb([
            ('verb', 'go'),
            ('direction', 'north')
        ]),
        ('verb', 'go')
    )
    # 'bear eat honey': ParserError
    assert_raises(
        parser.ParserError,
        parser.parse_verb,
        [('noun', 'bear'), ('verb', 'eat'), ('noun', 'honey')]
    )

def test_object():
    # 'north': object == 'north'
    assert_equal(
        parser.parse_object([
            ('direction', 'north')
        ]),
        ('direction', 'north')
    )
    # 'honey quickly': object == 'honey' ('quickly' irrelevant)
    assert_equal(
        parser.parse_object([
            ('noun', 'honey'),
            ('error', 'quickly')
        ]),
        ('noun', 'honey')
    )
    # 'the front': ParserError
    assert_raises(
        parser.ParserError,
        parser.parse_object,
        [('stop', 'the'), ('error', 'front')]
    )

# and now to test some whole sentences
def test_sentence():
    assert_equal(
        parser.parse_sentence([
            ('verb', 'go'),
            ('direction', 'north')
        ]).subject,
        'player'
    )
    assert_equal(
        parser.parse_sentence([
            ('verb', 'go'),
            ('direction', 'north')
        ]).verb,
        'go'
    )
    assert_equal(
        parser.parse_sentence([
            ('verb', 'go'),
            ('direction', 'north')
        ]).object,
        'north'
    )
    assert_raises(
        parser.ParserError,
        parser.parse_sentence,
        [('verb', 'eat'), ('verb', 'kill')]
    )

# let's try out our equality definitions!
def test_sentence_again():
    assert_equal(
        parser.parse_sentence([
            ('verb', 'go'),
            ('direction', 'north')
        ]),
        parser.Sentence(
            ('noun', 'player'),
            ('verb', 'go'),
            ('direction', 'north')
        )
    )
