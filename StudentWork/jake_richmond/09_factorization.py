# this script should take an integer up to 10000 as input and print
# the prime factorization of it as follows:
# 60 = 2^2 * 3 * 5
# Feel free to use the list of primes in primes.txt

from sys import argv

target = argv [1] 

# Make a list of primes from primes.txt
f = open('primes.txt')
primes = f.read().split('\n')
f.close()

remainder = int(target)
counts = {}

for p in primes:
	p = int(p)
	print p
	while remainder % p == 0:
		if p in counts: 
			counts[p] += 1
		else:
			counts[p] = 1
		remainder = remainder / p
	if remainder == 1:
		break

output = str(target) + "="
for factor in counts:
	output += str(factor)
	if counts[factor] > 1:
		output += "^" + str(counts[factor])
	output += " * "

print output[:-3] 