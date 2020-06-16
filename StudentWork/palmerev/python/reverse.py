# Using not built in function,
# and just square bracket list notation,
# reverse the set of characters

characters = "ABCDEF"
character_goal = "FEDCBA"

def reverse_characters(c):
    return c[::-1]

print(reverse_characters(characters))

# now do the same with words
# and use built in function
# like split join and reverse

words = "now is the time"
word_goal = "time the is now"

def reverse_words(words):
    rev_list = []
    word_list = words.split()
    for word in reversed(word_list):
        rev_list.append(word)

    return " ".join(rev_list)

print(reverse_words(words))

# Finally EXTRA CREDIT do the same with words
# and DO NOT use built in function
# like split join and reverse
def split(s, delimiter=" "):
    #TODO: fix skips last word
    str_list = []
    word = ""
    for i, char in enumerate(s):
        if char != delimiter:
            word += char
        else:
            str_list.append(word)
            word = ""
            last_delimiter_index = i
    str_list.append(s[last_delimiter_index+1:]) #get last word
    return str_list

def join(seq, delimiter=" "):
    outstring = ""
    for item in seq:
        outstring += str(item) + delimiter
    outstring = outstring[:-len(delimiter)]
    return outstring

def reverse_list(lst):
    outlist = []
    for i in range(len(lst)-1,-1,-1):
        outlist.append(lst[i])
    return outlist

def reverse_words_hard(words):
    lst = split(words, " ")
    rev_list = reverse_list(lst)
    output = join(rev_list)
    return output

print(reverse_words_hard(words))

