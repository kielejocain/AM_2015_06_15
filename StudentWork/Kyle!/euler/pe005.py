from sys import argv

def next_prime(primes):
    """This function computes and returns the smallest integer greater than
    but not divisible by a list of increasing integers."""
    output = primes[-1] + 1
    while True:
        if 0 not in [output % p for p in primes]:
            return output
        output += 1


def factorize(product):
    """Returns a dictionary with key: value pairs as factor: power"""
    primes = [2]
    factors = {}
    while product % 2 == 0:
        if 2 in factors:
            factors[2] += 1
        else:
            factors[2] = 1
        product /= 2
    while product > 1:
        primes.append(next_prime(primes))
        while product % primes[-1] == 0:
            if primes[-1] in factors:
                factors[primes[-1]] += 1
            else:
                factors[primes[-1]] = 1
            product /= primes[-1]
    return factors

if __name__ == '__main__':
    highest = int(argv[1])
    factorizations = []
    for i in range(2, highest + 1):
        factorizations.append(factorize(i))
    factors = []
    for num in factorizations:
        factors += num.keys()
    factors = list(set(factors))
    lcm = {}
    for num in factorizations:
        for factor in num:
            if factor in lcm:
                lcm[factor] = max(lcm[factor], num[factor])
            else:
                lcm[factor] = num[factor]
    output = 1
    for factor in lcm:
        output *= factor ** lcm[factor]
    print output
