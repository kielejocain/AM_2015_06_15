# this uses the "wikipedia" class from https://pypi.python.org/pypi/wikipedia/
# begins by ruling out the top 100 words plus conjugated forms of "to be" verbs that I have added, and the word "an." top 100 words are from https://en.wikipedia.org/wiki/Most_common_words_in_English

from wikipedia import *
import re #regular expression
from collections import Counter 

# creating a list of the top 100 English words, plus variations on the verb "to be"

top_file = open('100words.txt')

top100 = []

for line in top_file: 
	items = line.split() 
	top100.append(items[1]) #the text file I made has the order number as the first line and I'm too lazy to take it out.

# print "these are the 100 most common words: " 
# print top100	

def top_words_tuples(topic, number):
	raw_words = wikipedia.page(topic).content.split() 
	topic_words = []
	for word in raw_words:
		try:
			just_word = re.sub("[^a-zA-Z]+", "", word).lower()
			topic_words.append(str(just_word)) # there's a bunch of unicode-related junk that gets tacked on that this attempts to eliminate
		except UnicodeEncodeError:
			pass
			
	topic_freq = {}

	for word in topic_words:
		if word not in top100 and len(word) > 1:
			if word in topic_freq.keys():
				topic_freq[word] = topic_freq[word] + 1
			else:
				topic_freq[word] = 1
			

	# print "-" * 15
	# print "these are the top", number, "words in the article on", topic, "that are not in the top 100 English words: "
	
	if len(topic_freq) > number:
		return Counter(topic_freq).most_common()[:number]
	else:
		return Counter(topic_freq).most_common()
	
def top_words(topic, number):
	output = []
	for item in top_words_tuples(topic, number):
		output.append(item[0])
	return output
		
print "Welcome to the Top Words program!"
print "This program uses Wikipedia pages to determine words related to the subject of your choice."

print "What subject would you like a list for?"
input_needed = True
while input_needed:
	try:
		subj = raw_input(">>  ")
		print "Searching, please wait..."
		wikipedia.page(subj)
		valid_subj = subj
		input_needed =  False
	except PageError:
		print "Wikipedia page of that title not found. Please try a different name for your topic."
	except DisambiguationError as de:
		print "-----> ~", subj, "~ could refer to any of these articles:"
		for item in de.options:
			try:
				print str(item)
			except UnicodeEncodeError:
				pass
		print "Please type the name of the article you would like to use exactly as it appears above."
		
print "How many words would you like to see?"
input_needed = True
while input_needed:
	try:
		numb = int(raw_input(">>  "))
		input_needed = False
	except ValueError:
		print "please enter a valid integer number"
		
print "Finding words, this may take a minute..."
print top_words(valid_subj, numb)

