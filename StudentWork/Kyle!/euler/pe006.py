from sys import argv

n = int(argv[1])

sum_n = n * (n + 1) / 2
sum_squares = n * (n + 1) * (2 * n + 1) / 6

print str(sum_n ** 2 - sum_squares)
