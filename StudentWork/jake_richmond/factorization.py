import sys
n = int(sys.argv[1])
result = []
for i in xrange(2,n):
    while n % i == 0:
        #print i,"|",n
        n = n/i
        result.append(i)

    if n == 1: 
        break

if n > 1: result.append(n)
print result