from math import sqrt

def distance(x, y):
    return sqrt((x*x + y*y))

def find_nearest(location_ltr, locations, n):
    results = []
    for loc in locations:
        if loc[2] == location_ltr.upper():
            curr_location = loc
            break
    for loc in locations:
        letter = loc[2]
        x_diff = abs(loc[0] - curr_location[0])
        y_diff = abs(loc[1] - curr_location[1])
        relative_distance = distance(x_diff, y_diff)
        results.append((relative_distance, letter))

    results.sort()
    return results[1:n+1]


data = [[531, 408, 'A'], [225, 52, 'B'], [594, 242, 'C'], [351, 102, 'D'], [371, 15, 'E'], [569, 353, 'F'],
        [342, 39, 'G'], [218, 304, 'H'], [428, 260, 'I'], [329, 158, 'J'], [585, 530, 'K'], [71, 114, 'L'],
        [587, 88, 'M'], [347, 180, 'N'], [180, 332, 'O'], [250, 522, 'P'], [88, 475, 'Q'], [260, 128, 'R'],
        [328, 505, 'S'], [381, 201, 'T'], [360, 192, 'U'], [414, 313, 'V'], [525, 293, 'W'], [240, 563, 'X'],
        [117, 546, 'Y'], [507, 127, 'Z']]
square_size = 600

current_location = 'G'
top_five_nearest = find_nearest(current_location, data, 5)
top_five_letters = [x[1] for x in top_five_nearest]
style = """
<style>
    #box { background:blue; position:relative; }
    #box span { color:white; position:absolute; }
</style>
"""
f = open("positions.html", "w")
f.write(style)
f.write('<div id="box" style="width:{0}px;height:{0}px;">\n'.format(square_size))
for item in data:
    if item[2] == current_location:
        f.write('<span style="left:{x}px; top:{y}px; color:red;"> {v} </span>\n'.format(
            x=item[0], y=item[1], v=item[2]
            )
        )
    elif item[2] in top_five_letters:
        f.write('<span style="left:{x}px; top:{y}px; color:orange;"> {v} </span>\n'.format(
            x=item[0], y=item[1], v=item[2]
            ))
    else:
        f.write('<span style="left:{x}px; top:{y}px;"> {v} </span>\n'.format(x=item[0], y=item[1], v=item[2]))
f.write("</div>\n")
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
