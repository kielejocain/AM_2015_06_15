# Using not built in function,
# and just square bracket list notation,
# reverse the set of characters

characters = "ABCDEF"
character_goal = "FEDCBA"

def reverse_characters(characters):
    reversed = characters[::-1]
    return

print(reverse_characters(characters))

# now do the same with words
# and use built in function
# like split join and reverse

words = "now is the time"
word_goal = "time the is now"

def reverse_words(words):
    word = []
    word = words.split(" ")
    return " ".join(word[::-1])

print(reverse_words(words))

# Finally EXTRA CREDIT do the same with words
# and DO NOT use built in function
# like split join and reverse

def reverse_words_hard(words):
    list = []
    goal = ""
    for word in words:
        list += word
        for index in range(len(list)-1, -1, -1):
            word_goal = list[i] + " "

    return

print(reverse_words_hard(words))
