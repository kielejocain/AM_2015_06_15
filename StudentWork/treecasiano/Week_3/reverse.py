# Using not built in function,
# and just square bracket list notation,
# reverse the set of characters

characters = "ABCDEF"
character_goal = "FEDCBA"

def reverse_characters(characters):
    # return characters[::-1]   this is Pythonic, but not available in other langauges
    output = ""
    for c in characters:
        output = c + output
    return output
print(reverse_characters(characters))

# now do the same with words
# and use built in function
# like split join and reverse

words = "now is the time"
word_goal = "time the is now"

def reverse_words(words):
    reversed_phrase_list = words.split()
    return " ".join(reversed_phrase_list[::-1])
print(reverse_words(words))

# Finally EXTRA CREDIT do the same with words
# and DO NOT use built in function
# like split join and reverse

def reverse_words_hard(words):
    temp_list = []
    word = ""
    deliminator = " "
    for c in words:
        if c == deliminator:
            temp_list.append(word)
            word = ""
        else:
            word += c
    temp_list.append(word)

    output = ""
    first_word = True

    for word in temp_list:
        if first_word:
            output = word
            first_word = False
        else:
            output = word + ' ' + output

    return output

print(reverse_words_hard(words))

