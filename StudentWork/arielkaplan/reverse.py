# Using not built in function,
# and just square bracket list notation,
# reverse the set of characters

characters = "ABCDEF"
character_goal = "FEDCBA"

def reverse_characters(characters):
    result = characters[::-1]
    return result

print(reverse_characters(characters))

# now do the same with words
# and use built in function
# like split join and reverse

words = "now is the time"
word_goal = "time the is now"

def reverse_words(words):
    list_of_words = words.split(' ')
    reversed_list = list(reversed(list_of_words))
    result = ' '.join(reversed_list)
    return result
print(reverse_words(words))

# Finally EXTRA CREDIT do the same with words
# and DO NOT use built in function
# like split join and reverse

def reverse_words_hard(words):
    list_of_words = []
    current_word = ''
    current_space_index = None

    # Split string into list of words
    for i in range(len(words)):
        char = words[i]
        if char != ' ':
            current_word += char
        elif char == ' ':
            list_of_words.append(current_word)
            current_space_index = i
            current_word = ''
        else:
            print "You shouldn't be here."
    # Grab final word
    last_word = words[current_space_index + 1:]
    list_of_words.append(last_word)

    # Reverse list
    reversed_list = list_of_words[::-1]

    # Join list
    reversed_words = ''
    for word in reversed_list:
        reversed_words += word + " "

    # Trim trailing space
    reversed_words = reversed_words[:-1]
    return reversed_words

print(reverse_words_hard(words))

