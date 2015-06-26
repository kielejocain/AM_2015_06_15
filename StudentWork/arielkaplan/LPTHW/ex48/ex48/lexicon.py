sentence = raw_input(">> ")

def scan(sentence):
	words = sentence.split()

	dictionary = {
		"direction": ["north", "south", "east", "west"]
		# Add other types of words later
	}

	for word in words:
		

	for key in dictionary:
		for entry in dictionary[key]:
			if word == entry:
				return (key, entry)
			else:
				return "Try again"
