# Using not built in function,
# and just square bracket list notation,
# reverse the set of characters

characters = "ABCDEF"
character_goal = "FEDCBA"

def reverse_characters(characters):
    return characters[::-1]

print(reverse_characters(characters))

# now do the same with words
# and use built in function
# like split join and reverse

words = "now is the time"
word_goal = "time the is now"


def reverse_words(words):
    wlist = words.split(" ")
    wlist.reverse()
    new = (" ").join(wlist)
    return new

print(reverse_words(words))

# Finally EXTRA CREDIT do the same with words
# and DO NOT use built in function
# like split join and reverse

def reverse_words_hard(words):
    # DO WORK HERE ...
    return

print(reverse_words_hard(words))
