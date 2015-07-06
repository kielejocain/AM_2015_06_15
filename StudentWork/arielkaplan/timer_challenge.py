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
    def increment(self, addl_seconds=1):
        # find total seconds
        total_seconds = self.seconds + addl_seconds
        # pull minutes
        minutes = total_seconds / self.SECONDS_IN_MINUTE
        self.seconds = total_seconds % self.SECONDS_IN_MINUTE
        # call minutes function w/ minute value
        if minutes > 0:
            self.increment_minutes(minutes)

    def increment_minutes(self, addl_minutes=1):
        total_minutes = self.minutes + addl_minutes
        hours = total_minutes / self.MINUTES_IN_HOUR
        self.minutes = total_minutes % self.MINUTES_IN_HOUR
        if hours > 0:
            self.increment_hours(hours)

    def increment_hours(self, addl_hours=1):
        self.hours += addl_hours

    # remove one second
    def decrement(self, removed_seconds=1):
        # subtract removed seconds from current seconds
        total_seconds = self.seconds - removed_seconds
        # if still 0 or more, update current seconds; done.
        if total_seconds >= 0:
            self.seconds = total_seconds
        else:
            # if < 0, find # of minutes, and subtract remainder from 60
            total_seconds = abs(total_seconds)
            # it's already < 0, so at least 1 minute must be removed.
            minutes = (total_seconds / self.SECONDS_IN_MINUTE) + 1
            remainder_seconds = total_seconds % self.SECONDS_IN_MINUTE
            self.seconds = self.SECONDS_IN_MINUTE - remainder_seconds
            if minutes > 0:
                self.decrement_minutes(minutes)

    def decrement_minutes(self, removed_minutes=1):
        total_minutes = self.minutes - removed_minutes
        if total_minutes >= 0:
            self.minutes = total_minutes
        else:
            total_minutes = abs(total_minutes)
            hours = (total_minutes / self.MINUTES_IN_HOUR) + 1
            remainder_minutes = total_minutes % self.MINUTES_IN_HOUR
            self.minutes = self.MINUTES_IN_HOUR - remainder_minutes
            if hours > 0:
                self.decrement_hours(hours)

    def decrement_hours(self, removed_hours=1):
        self.hours -= removed_hours
        if self.hours < 0:
            return "Time's up!"


def test_timer():
    t = Timer()
    t.minutes = 59
    t.seconds = 59
    print (t, t.hours, t.minutes, t.seconds)
    t.increment()
    print(t, t.hours, t.minutes, t.seconds)
    t.decrement()
    print(t, t.hours, t.minutes, t.seconds)
    # t.increment(120)
    # print(t, t.hours, t.minutes, t.seconds)
    t.decrement(30)
    print(t, t.hours, t.minutes, t.seconds)
    t.increment(6000)
    print(t, t.hours, t.minutes, t.seconds)
    t.decrement(10800) # 3 hours
    print(t, t.hours, t.minutes, t.seconds)
    t.decrement(300)
    print(t, t.hours, t.minutes, t.seconds)


test_timer()

# EXTRA CREDIT: Deal with incrementing by an arbitrary amount, e.g. 60 or 120.
