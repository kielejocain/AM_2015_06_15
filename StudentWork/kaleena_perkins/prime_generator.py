from sys import argv

target = raw_input("Give me a number and I'll give you its prime numbers \n")

f = open('primes.txt')
prime = f.read().split('\n')[:-1]

f.close()

remainder = int(target)
counts = {}


for p in prime:
	p = int(p)
	while remainder % p == 0:
		if p in counts:
			counts[p] += 1
		else:
			counts[p] = 1
		remainder = remainder / p
	if remainder == 1:
		break
		
for i in counts:
	print "The prime number ", i, " appears", counts[i], " times."
			
