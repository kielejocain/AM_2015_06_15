#   TODO:
#   1.  Add increment and decrement methods for minutes and hours.
#   2.  If Seconds is at 59 and you increment:
#           A.  set seconds to zero
#           B.  increment minute
#   3.  Likewise if minutes is 59 set to zero and increment minutes
#   4.  Do similar work for hours.

class Timer(object):
    MINUTES_IN_HOUR = 60
    SECONDS_IN_MINUTE = 60

    def __init__(self, hours=None, minutes=None, seconds=None):
        if hours:
            self.hours = hours
        else:
            self.hours = 0

        if minutes:
            self.minutes = minutes
        else:
            self.minutes = 0

        if seconds:
            self.seconds = seconds
        else:
            self.seconds = 0

    def current_time(self):
        print "The time is now", self.hours, ":", self.minutes, ":", self.seconds

    def incr_check(self, new_time, this_unit):
        if this_unit == 'minutes':
            while new_time < 0:
                self.hours -= 1
                new_time += 60
            while new_time >= 60:
                self.hours += 1
                new_time -= 60
            self.minutes = new_time

        elif this_unit == 'seconds':
            while new_time < 0:
                self.minutes -= 1
                new_time += 60
            while new_time >= 60:
                self.minutes += 1
                new_time -= 60
            self.seconds = new_time

    # add one second
    def increment(self, amount=None, unit=None):
        if amount is None:
            amount = 1
        if unit is None:
            unit = 'seconds'

        if unit == 'seconds':
            self.seconds += amount
        elif unit == 'minutes':
            self.minutes += amount

        print "Printing unchecked time."
        print self.current_time()

        self.incr_check(self.seconds, 'seconds')
        self.incr_check(self.minutes, 'minutes')

        print "printing checked time."
        print self.current_time()

    # remove one second
    def decrement(self):
        self.seconds -= 1


# def test_timer():
#     t = Timer()
#     t.minutes = 59
#     t.seconds = 59
#     t.increment()
#     print(t, t.hours, t.minutes, t.seconds)
#
#
# test_timer()

while True:
    print "Please enter the number of hours, minutes and seconds you would like the clock to start at:\n"
    try:
        hrs = int(raw_input("Hours:  "))
        mins = int(raw_input("Minutes:  "))
        secs = int(raw_input("Seconds:  \n"))
        if hrs > 23 or mins > 59 or secs > 59: #  also raise error for less than 0
            raise ValueError
    except (TypeError, ValueError):
        print "Please enter valid numbers for the times.\n"
        continue
    print "Creating clock at", hrs, ":", mins, ":", secs, "...\n"

    clock = Timer(hrs, mins, secs)

    while True:
        print "What do you want to do?"
        print "1.  change the time on the clock"
        print "2.  start over with a new clock"
        print "3.  Exit the program"

        selection = raw_input("  >>  ")

        if selection == "1":
            print "How much do you want to change the time?"
            print "Use positive numbers to add time and negative numbers to subtract."
            while True:
                try:
                    mins = int(raw_input("Minutes:  "))
                    secs = int(raw_input("Seconds:  "))

                    clock.increment(mins, 'minutes')
                    clock.increment(secs, 'seconds')
                    break
                except (ValueError, TypeError):
                    print "please enter valid numbers"

            print clock.current_time()

        if selection == "2":
            break

        if selection == "3":
            print "Thanks for using the clock!"
            print "******** Goodbye! ********"
            exit()
