# This simple script demonstrates Python's ability to ignore poorly-written
# but uncalled functions.  As long as `bad_function` isn't used, the script
# runs without issue.  If you uncomment line 16, though...

def bad_function():
    if cheese:
        # there is no way the next line can work; regardless of the type of
        # `cheese`, you can't add an integer and then a string to it.
        cheese = cheese + 0 + "wonk"

def good_function(x):
    return x + ' is good!'

print good_function('cheese')

print bad_function("coding")
