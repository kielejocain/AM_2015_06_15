from sys import argv

f = open('primes.txt')
# reads the text file and splits it into a list on the line breaks
primes = f.read().split('\n')
f.close()

target = int(raw_input("What number do you wish to factor? >>  "))

# initializing remainder variable
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
    if remainder == 1:
        break

print counts