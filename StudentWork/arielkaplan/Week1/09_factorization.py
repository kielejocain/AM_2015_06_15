# this script should take an integer up to 10000 as input and print
# the prime factorization of it as follows:
# 60 = 2^2 * 3 * 5
# Feel free to use the list of primes in primes.txt

f = open('primes.txt')
# Save primes in a list (of strings)
primes = f.read().split("\n")[:-1]
f.close()

# accept any integer up to 10000
# check if evenly divisible by each prime (converted to integer)
# when yes:
#	save the prime in a list
#	divide number by prime
#	start over with new divided number from the beginning of prime list

number = int(raw_input("Give me an integer up to 10000. > "))
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

# Kyle's result:

# from sys import argv

# target = int(argv[1])

# f = open('primes.txt')
# primes = f.read().split("\n")[:-1]
# f.close()

# remainder = target
# counts = {}

# for p in primes:
# 	p = int(p)
# 	while remainder % p == 0 :
# 		if p in counts : 
# 			counts[p] += 1
# 		else :
# 			counts[p] = 1
# 		remainder = remainder/p
# 	if remainder == 1 :
# 		break

