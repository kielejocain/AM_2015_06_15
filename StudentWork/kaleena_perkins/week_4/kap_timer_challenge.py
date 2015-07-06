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
        if self.seconds == 60:
			self.increment_minute()
			self.seconds = 0

    # remove one second
    def decrement(self):
        self.seconds -= 1
        
    # # add one minute
    def increment_minute(self):
        self.minutes += 1
        if self.minutes == 60:
			self.increment_hour()
			self.minutes = 0
			
        
    # remove one minute
    def decrement_minute(self):
        self.minutes -= 1
        
    # add one hour
    def increment_hour(self):
        self.hours += 1

	# remove one hour
    def decrement_hour(self):
        self.hours -= 1

def test_timer():
    t = Timer()
    t.minutes = 59
    t.seconds = 59
    t.increment()
    print('hours: %d, minutes: %d, seconds: %d' %(t.hours, t.minutes, t.seconds))


test_timer()
