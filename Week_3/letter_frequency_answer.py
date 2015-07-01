#  Task Description:
#      Display the number of times each letter occurs.
#
#  What clarifying questions would you want to ask?
#
#  What types of data structures will we need?

sentence = "Now is the time for all good people to come to the aid of their planet."

output = {}
for c in sentence:
    if c not in output.keys():
        output[c] = 0
    output[c] += 1
print(output)

#  What if we want to count capitals and lower as the same?

output = {}
for c in sentence:
    uc = c.upper()
    if uc not in output.keys():
        output[uc] = 0
    output[uc] += 1
print(output)

#  What if we only want to track A-Z and not punctuation?
output = {}
output_list = []
for i in range(ord("A"), ord("Z") + 1):
    letter = chr(i)
    item = [0, letter]
    output[letter] = item
    output_list.append(item)

for c in sentence:
    uc = c.upper()
    if uc in output.keys():
        output[uc][0] += 1
print(output_list)
print(sorted(output_list))

#  What if we only want to report on a given set of letters?
output = {}
wanted = "AEIOU"
for c in sentence:
    uc = c.upper()
    if uc in wanted:
        if uc not in output.keys():
            output[uc] = 0
        output[uc] += 1
print(output)

#  What if we wanted to know about letters that occured zero times?
#  How could we order these by frequency?
#  How could we do this with words?
#  How could we visualize the counts in a horizontal bar chart?
#  How can we organize out code better to support reuse?
