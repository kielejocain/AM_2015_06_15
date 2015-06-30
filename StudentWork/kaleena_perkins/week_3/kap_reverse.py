# Using not built in function,
# and just square bracket list notation,
# reverse the set of characters

characters = "ABCDEF"
character_goal = "FEDCBA"

def reverse_characters(characters):
    return characters[-1::-1]

print(reverse_characters(characters))

# now do the same with words
# and use built in function
# like split join and reverse

words = "now is the time"
word_goal = "time the is now"

def reverse_words(words):
    word_list = words.split()
    reverse_list = []
    while len(word_list) > 0:
        item = word_list.pop(-1)
        reverse_list.append(item)
    sentence = " ".join(reverse_list)
    return sentence
print(reverse_words(words))

# Finally EXTRA CREDIT do the same with words
# and DO NOT use built in function
# like split join and reverse

def reverse_words_hard(words):
    sentence = ""
    for c in words:
        if c == " ":
            spot = words.index(c)
            sentence = " " + words[:spot] +  sentence
            words = words[spot + 1:]
    sentence = words + sentence
    return sentence

def reverse_words_hard_with_counter(words):
    sentence = ""
    counter = -1
    for c in words:
        counter += 1
        if c == " ":
            spot = counter
            sentence = words[:spot +1] + sentence
            words = words[spot + 1:]
            counter = -1
    sentence = words + " " +  sentence
    return sentence

print(reverse_words_hard(words))
print(reverse_words_hard_with_counter(words))

