f = open('primes.txt')
primes = f.read().split('\n')
f.close()


#create a dictionary

dict = {}

#take an integer input

input = int(raw_input("Please enter an integer from 1 to 10,000:  "))

n = int(input) # will this cause problems with n and input referring to the same thing? I don't think so

#??? some kind of massive while loop 

while n != 1:
	for fct_string in primes:
		factor = int(fct_string)
		exponent = 0 
		while n%factor == 0:
			exponent += 1
			n = n/factor
		if exponent != 0:
			dict[factor] = exponent
#create a dictionary with key as the prime number from primes and value as its exponent. will be end of a looping if statement
# create a string using the dictionary created above

output = str(input) + " = "

for key in dict:
	if dict[key] == 1:
		output += str(key) 
	else:
		output += str(key) + " ^ " + str(dict[key])
	output += " * "

output = output[:-3]
 
print output 