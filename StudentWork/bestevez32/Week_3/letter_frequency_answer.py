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
#  What if we wanted to know about letters that occurred zero times?

output = {}
# range scans the "sentence" , ord changes the letter to a number,
# range(1,5) = [1,2,3,4] , range(1,4+1) = [1,2,3,4]: This allows for the last letter to be "Z".
for i in range(ord("A"), ord("Z") + 1):
    letter = chr(i)
    output[letter] = 0

for c in sentence:
    uc = c.upper()
    if uc in output.keys():
        output[uc] += 1
print(output)

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

#  How could we order these by frequency?

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

#  How could we do this with words?
output = {}
words = sentence.split(" ")
for w in words:
    uc = w.upper()
    if uc not in output.keys():
        output[uc] = 0
    output[uc] += 1
print(output)

#  How could we visualize the counts in a horizontal bar chart?
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
ranked = sorted(output_list, reverse=True)

for item in ranked:
    print("{:<2} {:<4} {}".format(item[1], item[0], "X" * item[0]))

# How can we organize out code better to support reuse?
def get_alphabet():
    output_list = []

    for i in range(ord("A"), ord("Z") + 1):
        letter = chr(i)
        output_list.append(letter)
    return output_list


def key_list_to_dict(key_list, default_value):
    output = {}
    for key in key_list:
        output[key] = default_value
    return output


def dict_to_list(input_dict):
    output_list = []
    for k in input_dict.keys():
        item_list = [input_dict[k], k]
        output_list.append(item_list)
    return output_list


def count_letters(sentence):
    output = key_list_to_dict(get_alphabet(), 0)
    for c in sentence:
        uc = c.upper()
        if uc in output.keys():
            i = ord(uc)
            output[uc] += 1
    return output


def print_letters(output):
    output_list = dict_to_list(output)
    ranked = sorted(output_list, reverse=True)
    for item in ranked:
        print("{:<2} {:<4} |{}".format(item[1], item[0], "X " * item[0]))


print_letters(count_letters(sentence))
