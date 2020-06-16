print "VERSION 1"
numbers = []
def while_loop_function(max_num, incrementor):
    i = 0
    while i < max_num:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + incrementor
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i
    return numbers
while_loop_function(20, 2)

print "The numbers: "

for num in numbers:
    print num


# rewrite to use for-loops and range

print "VERSION 2"

def for_loop_function(max_num):
    i = 0
    more_numbers = range(0, max_num)
    for i in more_numbers:
        print "At the top i is %d" % i
        print "Numbers now: ", more_numbers
        print "At the bottom i is %d" % i
        print "The numbers: "
    for num in more_numbers:
        print num

for_loop_function(20)


