from sys import argv

sum = 0
for num in argv[1:]:
    num = int(num)
    sum += num
print sum
