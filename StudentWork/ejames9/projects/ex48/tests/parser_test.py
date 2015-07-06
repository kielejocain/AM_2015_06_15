from nose.tools import *
from ex48 import parser


def test_subject():
    # 'go north' starts with a verb: implied subject == 'player'
    assert_equal(
        parser.parse_subject([
            ('verb', 'go'),
            ('direction', 'north')
        ]),
        ('noun', 'player')
    )

    assert_equal(
        parser.parse_subject([
            ('noun', 'bear'),
            ('verb', 'eat'),
            ('noun', 'honey')
        ]),
        ('noun', 'bear')
    )

    assert_raises(
        parser.ParserError,
        parser.parse_subject,
        [('direction', 'back'), ('direction', 'north')] # args
    )


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
