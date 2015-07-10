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

    def change_time(self, num_seconds=None):
        if num_seconds is None:
            num_seconds = 0
        total_seconds = num_seconds + self.time_to_int()
        if total_seconds < 0:
            raise ValueError("attempted to create negative time")
        self.int_to_time(total_seconds)

    def int_to_time(self, num_seconds):
        self.hours = num_seconds / (Timer.SECONDS_IN_MINUTE * Timer.MINUTES_IN_HOUR)
        num_seconds -= self.hours * (Timer.SECONDS_IN_MINUTE * Timer.MINUTES_IN_HOUR)
        self.minutes = num_seconds / Timer.SECONDS_IN_MINUTE
        num_seconds -= self.minutes * Timer.SECONDS_IN_MINUTE
        self.seconds = num_seconds

    def time_to_int(self):
        total_seconds = 0
        total_seconds += self.seconds
        total_seconds += self.minutes * Timer.SECONDS_IN_MINUTE
        total_seconds += self.hours * Timer.SECONDS_IN_MINUTE * Timer.MINUTES_IN_HOUR
        return total_seconds

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

def test_change_time():
    t = Timer()
    print(t, t.hours, t.minutes, t.seconds)
    t.change_time(5)
    print(t, t.hours, t.minutes, t.seconds)
    t.change_time(55)
    print(t, t.hours, t.minutes, t.seconds)
    t.change_time(3600)
    print(t, t.hours, t.minutes, t.seconds)
    t.change_time(-75)
    print(t, t.hours, t.minutes, t.seconds)
    t.seconds = 59
    print(t, t.hours, t.minutes, t.seconds)
    t.change_time(1)
    print(t, t.hours, t.minutes, t.seconds)
#test_timer()

test_change_time()