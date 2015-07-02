from math import sqrt

data = [[531, 408, 'A'], [225, 52, 'B'], [594, 242, 'C'], [351, 102, 'D'], [371, 15, 'E'], [569, 353, 'F'],
        [342, 39, 'G'], [218, 304, 'H'], [428, 260, 'I'], [329, 158, 'J'], [585, 530, 'K'], [71, 114, 'L'],
        [587, 88, 'M'], [347, 180, 'N'], [180, 332, 'O'], [250, 522, 'P'], [88, 475, 'Q'], [260, 128, 'R'],
        [328, 505, 'S'], [381, 201, 'T'], [360, 192, 'U'], [414, 313, 'V'], [525, 293, 'W'], [240, 563, 'X'],
        [117, 546, 'Y'], [507, 127, 'Z']]
square_size = 600
style = """
<style>
    #box { background:blue; position:relative; }
    #box span { color:white; position:absolute; }
</style>
"""

def find_nearest(origin, list_of_locations, top_locations):
    # calculate distance to each neighbor
    for location in list_of_locations:
        for sublist in data:
            if sublist[2] == origin:
                origin_x_value = sublist[0]
                origin_y_value = sublist[1]
        list_of_closest_locations = []
        for item in list_of_locations:
            location_x_value = item[0]
            location_y_value = item[1]
            location_name = item[2]
            distance_from_origin = sqrt(((location_x_value - origin_x_value) ** 2) + ((location_y_value - origin_y_value) ** 2))
            list_of_closest_locations += [(distance_from_origin, location_name)]
    # print list_of_closest_locations
    print list_of_closest_locations
    # sort the list by that distance
    sorted_list = sorted(list_of_closest_locations)
    #  return the top N items from the list
    return sorted_list[1:top_locations + 1]

# OUTPUT html for "J" and 5 would show R D N U and T highlighted.
output = find_nearest("J", data, 5)
print "\n\nTOP CLOSEST:  \n", output

# LIST OF TOP FIVE LOCATION LETTERS
top_items = []
for item in output:
    top_items.append(item[1])

# HTML OUTPUT
f = open("positions.html", "w")
f.write(style)
f.write('<div id="box" style="width:{0}px;height:{0}px; font-weight: bold;">\n'.format(square_size))
for item in data:
    if item[2] == "J":
        f.write('<span style="left:{x}px; top:{y}px; color: #FF0000;"> {v} </span>'.format(x=item[0], y=item[1], v=item[2]))
    elif item[2] in top_items:
        f.write('<span style="left:{x}px; top:{y}px; color: #FFA500;"> {v} </span>'.format(x=item[0], y=item[1], v=item[2]))
    else:
        f.write('<span style="left:{x}px; top:{y}px;"> {v} </span>'.format(x=item[0], y=item[1], v=item[2]))
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