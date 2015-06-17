# this script should take an integer up to 10000 as input and print
# the prime factorization of it as follows:
# 60 = 2^2 * 3 * 5
# Feel free to use the list of primes in primes.txt

# This function is only used in the alternative method below.
def factor_print(counts, factor):
    output = str(factor)
    if counts[factor] > 1:
        output += "^" + str(counts[factor])
    return output


from sys import argv

target = int(argv[1])

# make a list of primes from primes.txt
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

output = str(target) + " = "
for factor in counts:
    output += str(factor)
    if counts[factor] > 1:
        output += "^" + str(counts[factor])
    output += " * "

print output[:-3]

# An alternative method below uses a "list comprehension" to build a list of
# factors and their exponents procedurally, element by element.  You can then
# `join` the list with the `join` method on " * ".

# factors = [factor_print(counts, factor) for factor in sorted(counts.keys())]
#
# print " * ".join(factors)
