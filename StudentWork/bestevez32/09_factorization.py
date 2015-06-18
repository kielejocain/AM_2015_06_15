# this script should take an integer up to 10000 as input and print
# the prime factorization of it as follows:
# 60 = 2^2 * 3 * 5
# Feel free to use the list of primes in primes.txt

from sys import argv

target = int(argv[1])

f = open('primes.txt')
primes = f.read().split('\n')[:-1]
f.close()

remainder = target 
counts = {}

for p in primes:
	p = int(p)
	while (remainder % p) == 0:
		if p in counts:
			counts[p] += 1
		else:
			counts[p] = 1
		remainder = remainder / p
	if remainder == 1:
		break 
		
print counts