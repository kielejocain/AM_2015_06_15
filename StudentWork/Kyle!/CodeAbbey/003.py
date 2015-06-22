f = open('003_data.txt')
length = int(f.readline())
sums = []
for i in range(0, length):
    summands = [int(x) for x in f.readline().split()]
    sums.append(summands[0]+summands[1])
print " ".join([str(x) for x in sums])
