
# TODO NEAREST "STARBUCKS"
# 1. Define a function that for arbitrary value e.g. "J" find the nearest N items e.g. 5
#   a. calculate the distance to each neighbor
#   b. sort the list by that distance
#   c. return the top N from the sorted list
# 2. Modify the draw code to highlight "top" items
#   a. add a style property for color
#   b. determine if this item is in the top 5
#   c. conditionally set the color bases on if its the top 5
#   d. also indicate the selected position e.g. "J" with another color

# OUTPUT html for "J" and 5 would show R D N U and T highlighted.

#CLUES - Ways of calculating distance between two points.
# dist = sqrt( (x2 - x1)**2 + (y2 - y1)**2 )
# dist = math.hypot(x2 - x1, y2 - y1)

from math import sqrt, hypot

# indexes
LATTITUDE = 0
LONGITUDE = 1
LETTER = 2

location_list = [[531, 408, 'A'], [225, 52, 'B'], [594, 242, 'C'], [351, 102, 'D'], [371, 15, 'E'], [569, 353, 'F'],
                 [342, 39, 'G'], [218, 304, 'H'], [428, 260, 'I'], [329, 158, 'J'], [585, 530, 'K'], [71, 114, 'L'],
                 [587, 88, 'M'], [347, 180, 'N'], [180, 332, 'O'], [250, 522, 'P'], [88, 475, 'Q'], [260, 128, 'R'],
                 [328, 505, 'S'], [381, 201, 'T'], [360, 192, 'U'], [414, 313, 'V'], [525, 293, 'W'], [240, 563, 'X'],
                 [117, 546, 'Y'], [507, 127, 'Z']]
square_size = 610

style = """
<style>
    #box { background:blue; position:relative; }
    #box span { color:silver; position:absolute; }
</style>
"""

output = []

output.append(style)
output.append('<div id="box" style="width:{0}px;height:{0}px;">\n'.format(square_size))
for location in location_list:
    output.append(
        '<span style="left:{left}px; top:{y}px;"> {v} </span>'.format(left=location[0], y=location[1], v=location[2]))

print("".join(output))
f = open("positions.html", "w")
f.write("".join(output))
f.close()
