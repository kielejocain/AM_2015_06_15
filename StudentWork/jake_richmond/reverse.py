# Using not built in function,
# and just square bracket list notation,
# reverse the set of characters
# try to solve this with no variables, use python built in fns?

characters = "ABCDEF"
character_goal = "FEDCBA"
c = characters
c = c[::-1]
print c


#######KEVIN'S ANSWER#######
#def reverse_characters(characters):
#    output_str = ''
#    for c in characters:
#        output_str = c + output_str
#    output = ''
#    return output_str

#print(reverse_characters(characters))

# now do the same with words
# and use built in function
# like split join and reverse

words = "now is the time"
word_goal = "time the is now"

def reverse_words(words):
    word_list = words.split(" ")
    word_list.reverse()
    return " " .join(word_list)

print(reverse_words(words))

# Finally EXTRA CREDIT do the same with words
# and DO NOT use built in function
# like split join and reverse

words = "now is the time"


def reverse_words_hard(words):
    if words[-1] is not ' ':
        words += " "
    output_str = ""
    word = " "
    for c in words:
        if c == ' ':
            output_str = word + output_str
            word = " "
        else:
            word = word + c

    return output_str[1:]

print "this is the hard way "
print(reverse_words_hard(words))

