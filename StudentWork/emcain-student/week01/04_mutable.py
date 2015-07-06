# here we'd like to explore the idea of mutable v. immutable data.

# strings are immutable.  They cannot be changed.
x = 'foo'
y = x # refers to the same area in memory. can check with id(y)
print x # foo
y += 'bar'
print x # still foo

# perhaps that went as you expected.
# lists, however, are mutable.  This can lead to unexpected behavior.
x = [1, 2, 3]
y = x # x and y now refer to the same place in memory 
print x # [1, 2, 3]
y += [3, 2, 1]
print x # [1, 2, 3, 3, 2, 1]

# did that last line surprise you?

# another place this can bite you is inside function calls, where you might
# forget the details of what your function did to the arguments.

def adder(str):
    str += 'bar'

x = 'foo'
y = x
print x # foo
adder(y)
print y # foobar
print x # yep, still foo

def adder2(lst):
    lst += [3, 2, 1]

x = [1, 2, 3]
y = x
print x # [1, 2, 3]
adder2(y)
print y # [1, 2, 3, 3, 2 ,1]
print x # yep, it's weird again.
