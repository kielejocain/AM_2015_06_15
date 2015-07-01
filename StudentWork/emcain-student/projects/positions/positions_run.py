from positions import pythagoras

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
f = open("positions.html", "w")
f.write(style)
f.write('<div id="box" style="width:{0}px;height:{0}px;">\n'.format(square_size))
for item in data:
    f.write('<span style="left:{x}px; top:{y}px;"> {v} </span>'.format(x=item[0], y=item[1], v=item[2]))
f.write("</div>\n")
f.close()

# TODO NEAREST "STARBUCKS"
# 1. Define a function that for arbitrary value e.g. "J" find the nearest N items e.g. 5
#   a. calculate the distance to each neighbor

def calc_distances(my_position, vals):
    pyth = pythagoras.Pythagoras()
    # dists = {}
    distuples = []
    my_x = my_position[0]
    my_y = my_position[1]
    for coordinate in vals:
        dists[coordinate[2]] = pyth.distance(my_x, my_y, coordinate[0], coordinate[1])
    return dists

print "distances for point A"
dists_a = calc_distances(data[0], data)
print dists_a

print "distances for point B"
dists_b = calc_distances(data[1], data)
print dists_b

#   b. sort the list by that distance

# def dist_sort(distance_dict, num=None):
#     if num is None:
#         num = len(distance_dict)
#     distuples = [(distance_dict['A'], 'A')]
#     print "added tuple", (distance_dict['A'], 'A'), "to distuples."
#     for point in distance_dict:
#         #create a tuple
#         tup = (distance_dict[point], point)
#         #insert into list based on its sort order
#         for entry in distance_dict:
#             tup = (distance_dict[entry], entry)
#             for item in distuples:
#                 if tup[0] < item[0]:
#                     distuples.insert(distuples.index(entry), tup)
#                 print "added tuple", tup, "to distuples at index", distuples.index(item)
#             else:
#                 distuples.append(tup)
#                 print "added tuple", tup, "to end of distuples."
#     distuples = distuples[:num]
#     return distuples

print "sorted list for a"
print dist_sort(dists_a)

print "top 5 for b"
print dist_sort(dists_b, 5)

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