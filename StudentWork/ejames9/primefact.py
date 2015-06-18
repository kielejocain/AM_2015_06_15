
from sys import argv

target = argv[1]

f = open('primes.txt')
primes = f.read().split('\n')[:-1]
f.close()

remainder = target
counts = {}

for p in primes: 
p = int(p)
	while remainder % p == 0:
		if p in counts:
			counts[p] += 1
		else:
			counts[p] = 1
		remainder = remainder / p
	if remainder == 1
		break
