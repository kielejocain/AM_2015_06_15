from wikipedia import *
import re
from collections import Counter 

# creating a list of the top 100 English words, plus variations on the verb "to be"

top_file = open('100words.txt')

top100 = []

for line in top_file:
	items = line.split()
	top100.append(items[1])

# print "these are the 100 most common words: " 
# print top100	

def top_words_tuples(topic, number):
	raw_words = wikipedia.page(topic).content.split() # need to add error handling or an input loop here. 
	topic_words = []
	for word in raw_words:
		try:
			just_word = re.sub("[^a-zA-Z]+", "", word).lower()
			topic_words.append(str(just_word))
		except UnicodeEncodeError:
			pass
			
	topic_freq = {}

	for word in topic_words:
		if word not in top100 and word is not '':
			if word in topic_freq.keys():
				topic_freq[word] = topic_freq[word] + 1
			else:
				topic_freq[word] = 1
			

	# print "-" * 15
	# print "these are the top", number, "words in the article on", topic, "that are not in the top 100 English words: "
	
	return Counter(topic_freq).most_common()[:number]
	
def top_words(topic, number):
	output = []
	for item in top_words_tuples(topic, number):
		output.append(item[0])
	return output
		
print top_words('dog', 50)
print top_words('bicycle', 100)
print top_words('Barack Obama', 20)
	
