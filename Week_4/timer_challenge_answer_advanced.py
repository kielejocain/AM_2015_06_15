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

    # add one hour
    def increment_hours(self, amount):
        self.hours += amount
        if self.hours > 99:
            self.hours = 0

    # remove one hour
    def decrement_hours(self, amount):
        self.hours -= amount

    # add one minute
    def increment_minutes(self, amount):
        self.minutes += amount
        hours = int(self.minutes / self.MINUTES_IN_HOUR)
        self.increment_hours(hours)
        self.minutes = self.minutes % self.MINUTES_IN_HOUR

    # remove one minute
    def decrement_minutes(self, amount):
        self.minutes -= amount

    # add one second
    def increment(self, amount):
        self.seconds += amount
        minutes = int(self.seconds / self.SECONDS_IN_MINUTE)
        self.increment_minutes(minutes)
        self.seconds = self.seconds % self.SECONDS_IN_MINUTE

    # remove one second
    def decrement(self):
        self.seconds -= amount


def test_timer():
    t = Timer()
    t.minutes = 0
    t.seconds = 0
    t.increment(3661)
    print(t.hours, t.minutes, t.seconds)
    # Should get one hour zero minutes and zero seconds


test_timer()
