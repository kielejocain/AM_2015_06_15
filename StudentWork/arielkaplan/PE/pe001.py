# Project Euler: Multiples of 3 and 5

# If we list all the natural numbers below 10 that are multiples of 3 or 5, 
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

maximum = 1000
multiples = []
i = 1

while i < maximum :
	if (i % 3 == 0) or (i % 5 == 0) :
		multiples.append(i)
	i += 1

print multiples

total = 0
for n in multiples :
	total += n

print total
