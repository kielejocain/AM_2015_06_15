import string

# display the number of times each letter occurs
sentence = "Now is the time for all good people to come to the aid of their planet."


def basic_count(sentence):
    """returns dict of how many of each character"""
    letter_count = {}
    for char in sentence:
        if char not in letter_count:
            letter_count[char] = 0
        letter_count[char] += 1

    return letter_count

def fancy_count(sentence):
    """returns dict of all possible letters and no punctuation"""
    sentence = sentence.lower()
    alphabet = string.lowercase
    letter_count = {}
    # create dictionary of all letters set to 0
    for char in alphabet:
        letter_count[char] = 0
    for char in sentence:
        if char in letter_count.keys():
            letter_count[char] += 1
    print letter_count

fancy_count(sentence)