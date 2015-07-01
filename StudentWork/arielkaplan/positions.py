data = [[531, 408, 'A'], [225, 52, 'B'], [594, 242, 'C'], [351, 102, 'D'], [371, 15, 'E'], [569, 353, 'F'],
        [342, 39, 'G'], [218, 304, 'H'], [428, 260, 'I'], [329, 158, 'J'], [585, 530, 'K'], [71, 114, 'L'],
        [587, 88, 'M'], [347, 180, 'N'], [180, 332, 'O'], [250, 522, 'P'], [88, 475, 'Q'], [260, 128, 'R'],
        [328, 505, 'S'], [381, 201, 'T'], [360, 192, 'U'], [414, 313, 'V'], [525, 293, 'W'], [240, 563, 'X'],
        [117, 546, 'Y'], [507, 127, 'Z']]


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

from math import sqrt

def distance(current_position, neighbor):
    """takes two lists. returns distance"""
    X_COORD = 0
    Y_COORD = 1
    diff_x = abs(current_position[X_COORD] - neighbor[X_COORD]) # abs() --> make sure # is positive
    diff_y = abs(current_position[Y_COORD] - neighbor[Y_COORD])
    # distance = pythag(diff_x, diff_y) # options
    # distance = math.hypot(diff_x, diff_y) # options
    hypot = sqrt((diff_x **2) + (diff_y **2))
    return hypot

def all_distances(current_position, data):
    neighbor_distances = []
    for coord in data:
        LETTER_INDEX = 2
        distance_from_current = distance(current_position, coord)
        # create new tuple with (distance, letter)
        neighbor_distances.append((distance_from_current, coord[LETTER_INDEX]))

    return neighbor_distances

# print(all_distances([347, 180, 'N'], data))

def nearest_starbucks(current_pos_letter, data, how_many):
    LETTER_INDEX = 2

    for item in data:
        if item[LETTER_INDEX] == current_pos_letter:
            current_position = item[:]
            break

    distances = all_distances(current_position, data)
    ordered_by_distance = sorted(distances)
    # return closest #, not including self
    return ordered_by_distance[1:how_many + 1]

# print nearest_starbucks("J", data, 5)


square_size = 600
style = """
<style>
    #box { background:blue; position:relative; }
    #box span { color:white; position:absolute; }
</style>
"""
top_locs = nearest_starbucks("J", data, 5)
f = open("positions.html", "w")
f.write(style)
f.write('<div id="box" style="width:{0}px;height:{0}px;">\n'.format(square_size))
for item in data:
    for tup in top_locs:
        if item[2] == tup[1]:
            c = "color:yellow"
        else:
            c = ''
        f.write('<span style="left:{x}px; top:{y}px; {c};"> {v} </span>'.format(x=item[0], y=item[1], v=item[2], c=c))
f.write("</div>\n")
f.close()

# EXTRA CREDIT: draw a circle