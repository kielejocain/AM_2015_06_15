# display the number of times each letter occurs
sentence = "Now is the time for all good people to come to the aid of their planet."
from collections import Counter
letter_frequencies = Counter(sentence.upper().strip("."))
print "Using collections.Counter:"
print letter_frequencies.most_common()

letter_frequencies = {}
for i in range(26):
    letter_frequencies[chr(i + ord('A'))] = 0
for char in sentence:
    if char.isalpha():
        char = char.upper()
        letter_frequencies[char] += 1
print "Using regular dictionary:"
print Counter(letter_frequencies).most_common()

#Similar operations with words
plain_sentence = sentence.lower().strip(".")
words = plain_sentence.split()
word_count = {}
for word in words:
    if word not in word_count.keys():
        word_count[word] = 0
    word_count[word] += 1

print "word_count:", word_count