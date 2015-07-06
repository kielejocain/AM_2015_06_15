#  Task Description:
#      Display the number of times each letter occurs.
#
#  What clarifying questions would you want to ask?
#
#  What types of data structures will we need?

sentence = "Now is the time for all good people to come to the aid of their planet."
letter_set = ['a', 'b', 'c', 'd', 'e']


def find_set_list(sentence, letter_set):
    output = {}
    for c in sentence:
        c = c.lower()
        if c.isalpha() and (c in letter_set):
            if c not in output.keys():
                output[c] = 0
            output[c] += 1
    print(output)


def not_in_sentence(sentence):
    output = []
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    sentence = sentence.lower()
    for l in alphabet:
        if l not in sentence:
            output.append(l)
    print(output)

# This doesn't work yet
def sort_occurance(sentence):
    output = {}
    counter = 0
    for c in sentence:
        if c.isalpha():
			if c not in output.keys():
				output[c] = 0
			output[c] +=1
        for key in output:
			if output[key] == counter:
				print output[key]
			counter += 1


sort_occurance(sentence)
#  What if we want to count capitals and lower as the same?
#		use .lower() or .upper() before the loop or for each c
#  What if we only want to track A-Z and not punctuation?
#		is there some sort of alpha method built in? Yes .isalpha()
#  What if we only want to report on a given set of letters?
#		compare to the list and only report if c in list
#  What if we wanted to know about letters that occured zero times?
#		not_in_sentence(sentence)
#  How could we order these by frequency?
#		Maybe store the letter count in a list of list, then sort it?
#		sort_occurance()
#  How could we do this with words?
#  How could we visualize the counts in a horizontal bar chart?
#  How can we organize out code better to support reuse?
