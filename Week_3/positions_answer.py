from math import sqrt, hypot

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


def distance(point_from, point_to):
    LATTITUDE = 0
    LONGITUDE = 1
    lateral_distance = point_from[LATTITUDE] - point_to[LATTITUDE]
    longitudinal_distance = point_from[LONGITUDE] - point_to[LONGITUDE]
    return sqrt(lateral_distance ** 2 + longitudinal_distance ** 2)
    # return (hypot(p2[0] - p1[0], p2[1] - p1[1]))



letter_dict = {}
for d in data:
    letter = d[2]
    letter_dict[letter] = d

# for arbitrary value e.g. "J" find the nearest N items e.g. 5
def get_top(data, letter, top_n):
    selected = letter_dict[letter]
    # Calculate distance and append as 4th element after lat, long, and letter
    for location in data:
        dist = distance(location, selected)
        location.append(dist)

    s = sorted(data, key=lambda item: item[3])
    return s[0:top_n + 1]


top = get_top(data, "V", 5)
f = open("positions.html", "w")
f.write(style)
f.write('<div id="box" style="width:{0}px;height:{0}px;">\n'.format(square_size))
for item in data:
    if item in top:
        c = "color:yellow;"
    else:
        c = ""
    f.write('<span style="left:{left}px; top:{y}px;{c}"> {v} </span>'.format(left=item[0], y=item[1], v=item[2], c=c))

f.close()

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

# CLUES - Ways of calculating distance between two points.
# dist = sqrt( (x2 - x1)**2 + (y2 - y1)**2 )
# dist = math.h
