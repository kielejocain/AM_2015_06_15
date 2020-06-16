from wikipedia import *
import re
from collections import Counter 

top_file = open('100words.txt')

top100 = []

for line in top_file:
	items = line.split()
	top100.append(items[1])

print "these are the 100 most common words: " 
print top100	
	
raw_words = wikipedia.page('cats').content.split()
cats_words = []
for word in raw_words:
	try:
		just_word = re.sub("[^a-zA-Z]+", "", word).lower()
		cats_words.append(str(just_word))
	except UnicodeEncodeError:
		pass
		
cats_freq = {}

for word in cats_words:
	if word not in top100 and word is not '':
		if word in cats_freq.keys():
			cats_freq[word] = cats_freq[word] + 1
		else:
			cats_freq[word] = 1
			


print "-" * 15
print "these are the top 100 cat words that are not in the top 100 English words: "
top_cats_words = Counter(cats_freq).most_common()[:100]
print top_cats_words