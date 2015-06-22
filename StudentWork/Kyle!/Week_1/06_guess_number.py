# this script should generate a random integer of the appropriate size,
# then allow the user to take guesses until they guess correctly.
# Additional challenges:
#   1. Report the final guess count
#   2. Impose a maximum guess count
#   3. Allow the user to change the maximum using from sys import argv;
#           you'd call the script with python 06_guess_number.py <max>

from sys import argv
from random import randint

# pull the max and limit arguments from the script call if they exist.
# if they don't, max should be taken to be 100 and
# limit is set to the string 'inf'.  'inf' implies infinity (i.e., bigger
# than all integers), because I'm abusing the fact that in Python all strings
# are considered larger than all integers.
if len(argv) > 2:
    max = int(argv[1])
    limit = int(argv[2])
elif len (argv) == 2:
    max = int(argv[1])
    limit = 'inf'
# if no arguments are passed:
else:
    max = 100
    limit = 'inf'

# generate our random target
target = randint(1, max)
# track the minimum feasible guess
min = 1
guess = int(raw_input(
    "Pick a number between %d and %d. > " % (min, max)
))
# count the number of guesses
count = 1

# keep looping until you guess correctly or run out of time
while guess != target and count < limit:
    if guess < target:
        print "The number I'm thinking of is higher."
        min = guess + 1 # don't guess lower than that
    else:
        print "The number I'm thinking of is lower."
        max = guess - 1 # don't guess higher than that
    guess = int(raw_input(
        "Pick another number between %d and %d. > " % (min, max)
    ))
    count += 1

if guess == target:
    print "You did it!  It took you %d guesses." % count
else:
    print "Sorry, you have no more tries.\nI was thinking of %d." % target
