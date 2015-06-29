# ask user for a topic and a number of words???

# ask user for a language (assume English is the first language)

# create a dictionary 

# for each word somehow determine its translation into the other language

for word in words:
	try:
		article = page(word)
	except:
		pass
	the_html = article.html()
	

# add a key-value pair 