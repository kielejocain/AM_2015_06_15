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
    def increment_seconds(self):
        self.seconds += 1
        if self.seconds == Timer.SECONDS_IN_MINUTE:
            self.increment_minutes()
            self.seconds = 0

    def increment_minutes(self):
        self.minutes += 1
        if self.minutes == Timer.MINUTES_IN_HOUR:
            self.increment_hours()
            self.minutes = 0

    def increment_hours(self):
        self.hours += 1

    # remove one second
    def decrement_seconds(self):
        self.seconds -= 1
        if self.seconds <= 0:
            self.decrement_minutes()
            self.seconds = Timer.SECONDS_IN_MINUTE - 1

    def decrement_minutes(self):
        self.minutes -= 1
        if self.minutes <= 0:
            self.decrement_hours()
            self.minutes = Timer.MINUTES_IN_HOUR - 1

    def decrement_hours(self):
        if self.hours > 0:
            self.hours -= 1
        else:
            raise ValueError("attempted to create negative time")


def test_timer():
    t = Timer()
    t.minutes = 59
    t.seconds = 59
    t.increment_seconds()
    print(t, t.hours, t.minutes, t.seconds)
    t.decrement_seconds()
    print(t, t.hours, t.minutes, t.seconds)
    t.hours = 0
    t.minutes = 59
    t.seconds = 0
    print(t, t.hours, t.minutes, t.seconds)
    t.increment_minutes()
    print(t, t.hours, t.minutes, t.seconds)
    t.seconds = 59
    print(t, t.hours, t.minutes, t.seconds)
    t.increment_seconds()
    print(t, t.hours, t.minutes, t.seconds)


test_timer()
