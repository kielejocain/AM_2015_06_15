# Largest prime factor

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

f = open('primes.txt')
# Save primes in a list (of strings)
primes = f.read().split("\n")[:-1]
f.close()

number = 600851475143
print "Let's factor the number " + str(number) + "."

factors = []
remainder = number
i = 0

while remainder > 1 :
	prime = int(primes[i])
	if remainder % prime == 0 :
		factors.append(prime)
		remainder /= prime
		print "remainder = " + str(remainder)
	else:
		i += 1
print "Here are the factors of " + str(number) + ": "
print factors
print factors[-1]

###################

number = 600851475143
print ("Let's factor the number " + str(number) + 
	" without using a list of primes.")

factors = []
remainder = number
divisor = 2

while remainder > 1 :
	if remainder % divisor == 0 :
		factors.append(divisor)
		remainder /= divisor
		print "remainder = " + str(remainder)
	else:
		divisor += 1
print "Here are the factors of " + str(number) + ": "
print factors
print factors[-1]
