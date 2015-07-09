# display the number of times each letter occurs
sentence = "Now is the time for all good people to come to the aid of their planet."

def letter_counter(sentence):
    output = {}
    graph = []
    for c in "abcdefghijklmnopqrstuvwxyz":
        output[c] = 0
    for char in sentence.lower():
        if char not in "!.,;: '":
            output[char] += 1
    for key in output.keys():
        graph.append(key + ":" + "="*(output[key]))
    graph.sort()

print output

print "\n".join(graph)



#with words

word_dict = {}
word_graph = []
for word in sentence.split():
    word_dict[word] = 0
for word in sentence.split():
	word_dict[word] += 1
for key in word_dict.keys():
	word_graph.append(key + ":" + "="*(word_dict[key]))
word_graph.sort()

print word_dict
print "\n".join(word_graph)


#  What if we only want to report on a given set of letters?
input_sentence = ""
report_on = ""
letter_counter = {}
def letter_counter_specific(input_sentence, report_on):
    for c in report_on:
        letter_counter[c] = 0
    for char in sentence:
        letter_counter[char] += 1




#  How could we order these by frequency?
