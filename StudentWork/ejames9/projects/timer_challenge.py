__author__ = 'ericfoster'

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
        if self.seconds == 60:
            self.min_increment()
            self.seconds = 0

    # remove one second
    def decrement(self):
        if self.seconds == 0:
            self.seconds = 59
            self.min_decrement()
        else:
            self.seconds -= 1

    def min_increment(self):
        self.minutes += 1
        if self.minutes == 60:
            self.hour_increment()
            self.minutes = 0

    def min_decrement(self):
        if self.minutes == 0:
            self.minutes = 59
            self.hour_decrement()
        else:
            self.minutes -= 1

    def hour_increment(self):
        self.hours += 1

    def hour_decrement(self):
        self.hours -= 1
        if self.hours < 0:
            self.hours = 0


def test_timer_inc():
    t = Timer()
    t.hours = 0
    t.minutes = 59
    t.seconds = 59
    t.increment()
    timer = (t.hours, t.minutes, t.seconds)
    print("%d Hours, %d Minutes and %d Seconds") % (t.hours, t.minutes, t.seconds)

def test_timer_dec():
    t = Timer()
    t.hours = 1
    t.minutes = 0
    t.seconds = 0
    t.decrement()
    timer = (t.hours, t.minutes, t.seconds)
    print("%d Hours, %d Minutes and %d Seconds") % (t.hours, t.minutes, t.seconds)


test_timer_inc()
test_timer_dec()
