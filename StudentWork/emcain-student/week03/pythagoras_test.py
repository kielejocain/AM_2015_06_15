__author__ = 'Emily'

import math

### takes 2 sets of x,y coordinates and calculates the distance between them.

class Pythagoras(object):

    def __init__(self):
        self.x1 = 0
        self.y1 = 0
        self.x2 = 0
        self.y2 = 0

    def distance(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        return math.sqrt((math.pow(float(self.x1) - float(self.x2), 2)) + (math.pow(float(self.y1) - float(self.y2), 2)))

# coord_A = raw_input("please enter the x and y coordinates of point A, separated by a space, and press enter. >> ")
#
# point_A = coord_A.split()
#
# coord_B = raw_input("please enter the x and y coordinates of point B, separated by a space, and press enter. >> ")
#
# point_B = coord_B.split()
#
# dist_x = abs(float(point_A[0]) - float(point_B[0]))
# dist_y = abs(float(point_A[1]) - float(point_B[1]))
#
# distance = math.sqrt(pow(dist_x, 2) + pow(dist_y, 2))

pyth = Pythagoras()
print pyth.distance(0, 0, 3, 4)

