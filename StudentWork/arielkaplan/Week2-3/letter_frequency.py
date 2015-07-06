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


#  How could we order these by frequency?
def letter_frequency(sentence, alphabet):
    """Returns list of tuples (count, letter)"""
    sentence = sentence.lower()
    letter_frequency = []
    for char in alphabet:
        counter = sentence.count(char)
        letter_frequency.append((counter, char))
        sorted_frequency = sorted(letter_frequency)
        sorted_frequency.sort(reverse=True)
    return sorted_frequency

print letter_frequency(sentence, alphabet)


#  What if we wanted to know about letters that occurred zero times?
def zero_count(sentence, alphabet, frequency):
    """
    Frequency is number of occurrences.
    Returns list of letters found 'frequency' times.
    """
    FREQ_INDEX = 0
    LETTER_INDEX = 1
    sentence = sentence.lower()
    letter_frequency = []
    output = []
    for char in alphabet:
        counter = sentence.count(char)
        letter_frequency.append((counter, char))
    for tup in letter_frequency:
        if tup[FREQ_INDEX] == frequency:
            output.append(tup[LETTER_INDEX])
    return output

print zero_count(sentence, alphabet, 0)


#  How could we do this with words?
def word_frequency(sentence):
    word_count = {}
    words = sentence.split(" ")
    for word in words:
        if word not in word_count.keys():
            word_count[word] = 0
        word_count[word] += 1
    # sort by frequency
    freq_sort = []
    for word in word_count.keys():
        freq_sort.append((word_count[word], word))
    freq_sort.sort(reverse=True)

    return freq_sort

print word_frequency(sentence)


#  How could we visualize the counts in a horizontal bar chart?
def chart_letters(sentence, alphabet):
    ordered_letters = letter_frequency(sentence, alphabet)
    COUNT_INDEX = 0
    LETTER_INDEX = 1
    for item in ordered_letters:
        print str(item[LETTER_INDEX].upper()) + " || " + ("X" * item[COUNT_INDEX])

print chart_letters(sentence, alphabet)

#  How can we organize our code better to support reuse?

