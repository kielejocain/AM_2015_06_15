# Using not built in function,
# and just square bracket list notation,
# reverse the set of characters

characters = "ABCDEF"
character_goal = "FEDCBA"

def reverse_characters(characters):
    # DO WORK HERE ...

    return 'ABCDEF'[::-1]


print(reverse_characters(characters))

# now do the same with words
# and use built in function
# like split join and reverse

words = "now is the time"
word_goal = "time the is now"

def reverse_words(words):
    # DO WORK HERE ...
    word_arrangement = words.split(" ")
    word_arrangement.reverse()
    new_arrangement = " ".join(word_arrangement)
    return new_arrangement

print(reverse_words(words))

# Finally EXTRA CREDIT do the same with words
# and DO NOT use built in function
# like split join and reverse

def reverse_words_hard(words):
    # DO WORK HERE ...
    y = []
    word = ""

    return

print(reverse_words_hard(words))



