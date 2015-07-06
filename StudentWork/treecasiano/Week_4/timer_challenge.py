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
    def increment_seconds(self, seconds_incremented):
        self.seconds += seconds_incremented
        while self.seconds >= 60:
            self.increment_minutes(1)
            self.seconds -= self.SECONDS_IN_MINUTE

    def increment_minutes(self, minutes_incremented):
        self.minutes += minutes_incremented
        while self.minutes >= 60:
            self.hours += 1
            self.minutes -= self.MINUTES_IN_HOUR

    # remove one second
    def decrement_seconds(self, seconds_decremented):
        self.seconds -= seconds_decremented
        while self.seconds < 0:
            self.decrement_minutes(1)
            self.seconds += self.SECONDS_IN_MINUTE

    def decrement_minutes(self, minutes_decremented):
        self.minutes -= minutes_decremented
        while self.minutes < 0:
            self.hours -= 1
            self.minutes += self.MINUTES_IN_HOUR






def test_timer():
    t = Timer()
    t.minutes = 59
    t.seconds = 59

    print(t, t.hours, t.minutes, t.seconds)
    t.increment_minutes(1)
    print(t, t.hours, t.minutes, t.seconds)
    t.decrement_seconds(1)
    print(t, t.hours, t.minutes, t.seconds)
    t.decrement_minutes(1)
    print(t, t.hours, t.minutes, t.seconds)
    t.increment_seconds(125)
    print(t, t.hours, t.minutes, t.seconds)
    t.increment_minutes(77)
    print(t, t.hours, t.minutes, t.seconds)
    t.decrement_seconds(341)
    print(t, t.hours, t.minutes, t.seconds)
    t.decrement_minutes(13)
    print(t, t.hours, t.minutes, t.seconds)

test_timer()
