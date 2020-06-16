# sentence = raw_input(">> ")

def scan(sentence):
	words = sentence.split()
	parsed = []
	lexicon = {
		"direction": ["north", "south", "east", "west"],
		"verb": ['go', 'eat', 'kill'],
		"stop": ['the', 'in', 'of'],
		"noun": ['bear', 'princess']
		# Add other types of words later
	}
	for word in words:
		if word.isdigit():
			parsed.append(("number", int(word)))
			continue
		for category in lexicon:
			if word in lexicon[category]:
				parsed.append((category, word))
				# word won't be in multiple categories
				break
		else:
			parsed.append(('error', word))
	return parsed