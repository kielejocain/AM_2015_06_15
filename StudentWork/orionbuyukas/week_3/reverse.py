# Using not built in function,
# and just square bracket list notation,
# reverse the set of characters

characters = "ABCDEF"
character_goal = "FEDCBA"

def reverse_characters(characters):
    reversed = characters[::-1]
    return reversed

def reverse_characters_oneline(characters):
    return "".join(characters[i]for i in xrange(len(characters)-1, -1,-1))



print(reverse_characters(characters))

output = ""
for c in characters:
    output = c + output
return output


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

word_list + words.split(" ")


# Finally EXTRA CREDIT do the same with words
# and DO NOT use built in function
# like split join and reverse

def reverse_words_hard(words):
    list = []
    goal = ""

    if c in words =
        list += word
        for index in range(len(list)-1, -1, -1):
            goal = list[i] + " "

    return

print(reverse_words_hard(words))





temp _list = []
word = ""
delimiter = " "
for c in words:
    if c == delimiter:
        temp_list.append(word)
        word = False
