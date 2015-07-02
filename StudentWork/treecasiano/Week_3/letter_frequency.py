# display the number of times each letter occurs
sentence = "Now is the time for all good people to come to the aid of their planet."

def remove_white_space(sentence):
    new_sentence = "".join(sentence.split())
    return new_sentence

# if we don't care about the letters not in the sentence and we're okay with including punctuation:
def count_characters(sentence):
    sentence = remove_white_space(sentence)
    letter_frequency = {}
    for c in sentence:
        if c in letter_frequency:
            letter_frequency[c] += 1
        else:
            letter_frequency[c] = 1
    return letter_frequency

print "\nA SIMPLE COUNT OF CHARACTERS:\n", count_characters(sentence)

# what if we want to count capitals and lower as the same?
def count_characters_lowercase(sentence):
    sentence = remove_white_space(sentence)
    letter_frequency = {}
    for c in sentence.lower():
        if c in letter_frequency:
            letter_frequency[c] += 1
        else:
            letter_frequency[c] = 1
    return letter_frequency

print "\nA SIMPLE COUNT OF LOWER CASE CHARACTERS:\n ", count_characters_lowercase(sentence)

# and if we want to order them by frequency?
def count_characters_sorted(sentence):
    sentence = remove_white_space(sentence)
    letter_frequency = {}
    for c in sentence.lower():
        if c in letter_frequency:
            letter_frequency[c] += 1
        else:
            letter_frequency[c] = 1
    sorted_keys = sorted(letter_frequency, key=letter_frequency.get, reverse=True)
    values_list = []
    for key in sorted_keys:
        values_list.append(letter_frequency[key])
    sorted_dict = zip(values_list, sorted_keys)
    return sorted_dict

print "\nCHARACTERS SORTED BY FREQUENCY:\n", count_characters_sorted(sentence)

# what if we only want to track A-Z and not punctuation?

def without_punctuation(sentence):
    sentence = remove_white_space(sentence)
    letter_frequency = {}
    for c in sentence:
        if c.isalpha():
            if c in letter_frequency:
                letter_frequency[c] += 1
            else:
                letter_frequency[c] = 1
    return letter_frequency

print "\nLIST OF CHARACTERS, EXCLUDING PUNCTUATION:\n", without_punctuation(sentence)

# what if we only want to report on a given set of letters?
def count_certain_letters(sentence, *argv):
    sentence = remove_white_space(sentence)
    letter_frequency = {}
    list_of_args = []
    for arg in argv:
        list_of_args.append(arg)
    for c in sentence:
        if c in list_of_args:
            if c in letter_frequency:
                letter_frequency[c] += 1
            else:
                letter_frequency[c] = 1

    return letter_frequency

print "\nCOUNTING CERTAIN LETTERS:\n", count_certain_letters(sentence, 'a', 'z')

# how could we do this with words?
def find_words(*argv):
    word_frequency = {}
    sentence_list = sentence.split(" ")
    print sentence_list
    list_of_words = []
    for arg in argv:
        arg = arg.lower()
        list_of_words.append(arg.lower())
    for word in sentence_list:
        word = word.lower()
        if word in list_of_words:
            if word in word_frequency:
                word_frequency[word] += 1
            else:
                word_frequency[word] = 1
    return word_frequency

print "\nCOUNTING CERTAIN WORDS:\n", find_words(sentence, "Now", "is")

# how could we visualize the counts in a horizontal bar chart?

# how can we organize our code better to support reuse?

