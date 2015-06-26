def string_to_ascii(s):
	output = [] #creates an empty list
	for c in s: #for each character in string s. Knows c is a character because strings are iterables with unit character
		v=ord(c) #converts the character to the "order" or ascii number value
		output.append(v) #method/function of the output method/function. append is a predefined function for lists. 
		print(bin(v)) #converts v to a binary and prints it. 
	return output # this is not part of the for loop.
	
print(string_to_ascii("ABC")) #the function has been defined and now we are calling it on "ABC" and printing what is returned. 
print(string_to_ascii("KEL"))