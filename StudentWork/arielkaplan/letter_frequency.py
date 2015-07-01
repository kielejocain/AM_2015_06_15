# display the number of times each letter occurs
sentence = "Now is the time for all good people to come to the aid of their planet."

letter_count = {}

for char in sentence:
    if char not in letter_count:
        letter_count[char] = 0
    letter_count[char] += 1

print letter_count