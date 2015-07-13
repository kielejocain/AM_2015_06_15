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
        if self.seconds == SECONDS_IN_MINUTE:
            self.minute +=1
            self.seconds = 0
                if self.minute == MINUTES_IN_HOUR:
                    self.hours += 1

    # remove one second
    def decrement(self):
        self.seconds -= 1
        if self.seconds == 0 and self.minutes >=1 or self.hours >= 1:
            self.minute -= 1
            self.seconds = 59
        if self.minutes == 0 and self.hours >= 1:
            self.hours = -1
            self.minutes = 59


def test_timer():
    t = Timer()
    t.minutes = 59
    t.seconds = 59
    t.increment()
    print(t, hours, t.minutes, t.seconds)


test_timer()



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
    HOURS_IN_DAY = 24

    def __init__(self):
        self.days = 0
        self.hours = 0
        self.minutes = 0
        self.seconds = 0

    # add one second
    def increment(self):
        self.seconds += 1
        if self.seconds > 59:
            self.increment_minutes()
            self.seconds = 0

    def increment_minutes(self):
        self.minutes += 1
        if self.minutes > 59:
            self.increment_hours()
            self.minutes = 0

    def increment_hours(self):
        self.hours += 1
        if self.hours > 24:
            self.increment_days()
            self.hours = 0

    def increment_days(self):
        self.days += 1


    # remove one second
    def decrement_seconds(self):
        self.seconds -= 1
        if self.seconds < 0 and self.minutes >=1 or self.hours >= 1:
            self.decrement_minutes()
            self.seconds = 59
        else:
            self.seconds = 0

    def decrement_minutes(self):
        self.minutes -= 1
        if self.minutes < 0 and self.hours >= 1:
            self.decrement_hours()
            self.minutes = 59
        else:
            self.minutes = 0

    def decrement_hours(self):
        self.hours -= 1
        if self.hours < 0 and self.days >=1:
            self.hours = 24
            self.days -= 1
        else:
            self.hours = 0

def test_timer():
    t = Timer()
    t.minutes = 59
    t.seconds = 59
    t.increment()
    print(t.hours, t.minutes, t.seconds)

def decrement_timer_test():
    t = Timer()
    t.seconds = 1
    t.minutes = 1
    t.hours = 1
    t.days = 1
    t.decrement_seconds()
    print "The time is: {} hours, {} minutes, {} seconds, {} days." .format(t.hours, t.minutes, t.seconds, t.days)



test_timer()
decrement_timer_test()


class Timer(object):
    MINUTES_IN_HOUR = 60
    SECONDS_IN_MINUTE = 60
    HOURS_IN_DAY = 24

    def __init__(self):
        self.days = 0
        self.hours = 0
        self.minutes = 0
        self.seconds = 0

    # add one second
    def increment(self):
        self.seconds += 1
        if self.seconds > 59:
            self.increment_minutes()
            self.seconds = 0

    def increment_minutes(self):
        self.minutes += 1
        if self.minutes > 59:
            self.increment_hours()
            self.minutes = 0

    def increment_hours(self):
        self.hours += 1
        if self.hours > 24:
            self.increment_days()
            self.hours = 0

    def increment_days(self):
        self.days += 1


    # remove one second
    def decrement_seconds(self):
        self.seconds -= 1
        if self.seconds < 0 and self.minutes >=1 or self.hours >= 1:
            self.decrement_minutes()
            self.seconds = 59
        else:
            self.seconds = 0

    def decrement_minutes(self):
        self.minutes -= 1
        if self.minutes < 0 and self.hours >= 1:
            self.decrement_hours()
            self.minutes = 59
        else:
            self.minutes = 0

    def decrement_hours(self):
        self.hours -= 1
        if self.hours < 0 and self.days >=1:
            self.hours = 24
            self.days -= 1
        else:
            self.hours = 0

#print current time
#input time
#timer countdown
#alarm method


def test_timer():
    t = Timer()
    t.minutes = 59
    t.seconds = 59
    t.increment()
    print(t.hours, t.minutes, t.seconds)

def decrement_timer_test():
    t = Timer()
    t.seconds = 1
    t.minutes = 1
    t.hours = 1
    t.days = 1
    t.decrement_seconds()
    print "The time is: {} hours, {} minutes, {} seconds, {} days." .format(t.hours, t.minutes, t.seconds, t.days)



test_timer()
decrement_timer_test()
