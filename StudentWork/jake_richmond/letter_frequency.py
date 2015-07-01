# display the number of times each letter occurs
sentence = "Now is the time for all good people to come to the aid of their planet."

count = {}
for letter in sentence:
    if count.has_key(letter):
        count[letter] += 1
    else:
        count[letter] = 1

for key in count:
    if count[key] > 1:
        print key, count[key]