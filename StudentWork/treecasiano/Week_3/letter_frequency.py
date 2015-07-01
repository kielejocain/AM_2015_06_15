# display the number of times each letter occurs
sentence = "Now is the time for all good people to come to the aid of their planet."
sentence = "".join(sentence.split())

# if we don't care about the letters not in the sentence and we're okay with including punctuation:
def count_characters():
    letter_frequency = {}
    for c in sentence:
        if c in letter_frequency:
            letter_frequency[c] += 1
        else:
            letter_frequency[c] = 1
    return letter_frequency

print count_characters()

# what if we want to count capitals and lower as the same?
def count_characters_lowercase():
    letter_frequency = {}
    for c in sentence.lower():
        if c in letter_frequency:
            letter_frequency[c] += 1
        else:
            letter_frequency[c] = 1
    return letter_frequency

print count_characters_lowercase()

# and if we want to order them by frequency?
def count_characters_sorted():
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
    sorted_dict = zip( values_list, sorted_keys)
    return sorted_dict

print count_characters_sorted()

# what if we only want to track A-Z and not punctuation?

# what if we only want to report on a given set of letters?

# how could we do this with words?

# how could we visualize teh counts in a horizontal bar chart?

# how can we organize our code better to support reuse?

