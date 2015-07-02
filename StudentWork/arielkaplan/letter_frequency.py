import string

# display the number of times each letter occurs
sentence = "Now is the time for all good people to come to the aid of their planet."
alphabet = string.lowercase
# alternate, more universal, probably faster *********
# alphabet = {}
# for i in range(ord("A"), ord("Z") + 1):
#     letter = chr(i)
#     alphabet[letter] = 0

wanted_letters = 'aeiou' # sample


def basic_count(sentence):
    """returns dict of how many of each character"""
    letter_count = {}
    for char in sentence:
        if char not in letter_count:
            letter_count[char] = 0
        letter_count[char] += 1
    return letter_count

basic_count(sentence)

#  EXTRA: What if we want to count capitals and lower as the same?
#  EXTRA: What if we only want to track A-Z and not punctuation?
def fancy_count(sentence, alphabet):
    """returns dict of all letters and no spaces or punctuation"""
    sentence = sentence.lower()

    # create dictionary of all letters set to 0
    letter_count = {}
    for char in alphabet:
        letter_count[char] = 0

    for char in sentence:
        if char in letter_count.keys():
            letter_count[char] += 1
    return letter_count

fancy_count(sentence, alphabet)


#  EXTRA: What if we only want to report on a given set of letters?
#  --basically the above, with modified alphabet list
def which_letters(sentence, wanted_letters):
    """counted letters as a string, e.g. 'aeiou'. Returns dict."""
    sentence = sentence.lower()

    # create dictionary of all letters set to 0
    letter_count = {}
    for char in wanted_letters:
        letter_count[char] = 0

    for char in sentence:
        if char in letter_count.keys():
            letter_count[char] += 1
    return letter_count

print which_letters(sentence, wanted_letters)


#  What if we wanted to know about letters that occurred zero times?
#  How could we order these by frequency?
def letter_count(sentence, alphabet, frequency):
    """frequency is number of occurrences"""
    sentence = sentence.lower()

    # create dictionary of all letters set to 0
    letter_count = {}
    for char in some_letters:
        letter_count[char] = 0

    for char in sentence:
        if char in letter_count.keys():
            letter_count[char] += 1
    return letter_count


#  How could we do this with words?
#  How could we visualize the counts in a horizontal bar chart?
#  How can we organize out code better to support reuse?

