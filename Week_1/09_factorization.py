# this script should take an integer up to 10000 as input and print
# the prime factorization of it as follows:
# 60 = 2^2 * 3 * 5
# Feel free to use the list of primes in primes.txt
from sys import argv
script, target = argv
num = int(target)
with open("primes.txt") as primes:
    lst = primes.read().split('\n')[:-1] #ignore the last line of the file

prime_list = [int(x) for x in lst]
factors = []
target = num
for x in prime_list:
    while num > 1 and num % x == 0:
        factors.append(x)
        num = num / x

#print "prime factors of %d are: " % target
strs = [str(x) for x in factors]
print "60 =", " * ".join(strs)
