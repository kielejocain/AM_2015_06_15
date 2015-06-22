from sys import argv

def next_prime(primes):
    """This function computes and returns the smallest integer greater than
    but not divisible by a list of increasing integers."""
    output = primes[-1] + 1
    while True:
        if 0 not in [output % p for p in primes]:
            return output
        output += 1

target = int(argv[1])

primes = [2]
left = target
while left % 2 == 0:
    biggest = 2
    left /= 2

while left > 1:
    primes.append(next_prime(primes))
    while left % primes[-1] == 0:
        biggest = primes[-1]
        left /= primes[-1]

print biggest
