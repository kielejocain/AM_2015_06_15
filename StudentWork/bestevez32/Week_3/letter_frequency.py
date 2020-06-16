# display the number of times each letter occurs
sentence = "Now is the time for all good people to come to the aid of their planet."

# 1.for letters in sentence split between letters and spaces
    # take the string and convert it to a dictionary

# 2. scan the letters in the sentence and account for the characters
    # keep count of the frequency of the letters


# Define a function for the letters in sentence

def histograms(sentence):

    # Creates an Empty Dictionary
    d = dict()
    # The for loop goes over the string.
    for c in sentence:
    # If the character c is not in the dictionary
        if c not in d:
    # A new item with the key c and initial val of 1 is created.
            d[c] = 1
    # If c is already in the dictionary we increment d [c]
        else:
            d[c] += 1

    return d

def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse

print histograms(sentence)




