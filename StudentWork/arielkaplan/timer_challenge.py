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

    def __init__(self):
        self.hours = 0
        self.minutes = 0
        self.seconds = 0

    # add one second
    def increment(self):
        self.seconds += 1
        if self.seconds == self.SECONDS_IN_MINUTE:
            self.minutes += 1
            self.seconds = 0
        if self.minutes == self.MINUTES_IN_HOUR:
            self.hours += 1
            self.minutes = 0

    # remove one second
    def decrement(self):
        self.seconds -= 1
        if self.seconds < 0:
            self.minutes -= 1
            self.seconds = 59
        if self.minutes < 0:
            self.hours -= 1
            self.minutes = 59



def test_timer():
    t = Timer()
    t.minutes = 59
    t.seconds = 59
    t.increment()
    print(t, t.hours, t.minutes, t.seconds)
    t.decrement()
    print(t, t.hours, t.minutes, t.seconds)


test_timer()
