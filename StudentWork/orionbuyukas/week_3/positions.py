from math import sqrt, hypot

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
#   b. sort the list by that distance
#   c. return the top N from the sorted list
# 2. Modify the draw code to highlight "top" items
#   a. add a style property for color
#   b. determine if this item is in the top 5
#   c. conditionally set the color bases on if its the top 5
#   d. also indicate the selected position e.g. "J" with another color

# OUTPUT html for "J" and 5 would show R D N U and T highlighted.






data = [[531, 408, 'A'], [225, 52, 'B'], [594, 242, 'C'], [351, 102, 'D'], [371, 15, 'E'], [569, 353, 'F'],
        [342, 39, 'G'], [218, 304, 'H'], [428, 260, 'I'], [329, 158, 'J'], [585, 530, 'K'], [71, 114, 'L'],
        [587, 88, 'M'], [347, 180, 'N'], [180, 332, 'O'], [250, 522, 'P'], [88, 475, 'Q'], [260, 128, 'R'],
        [328, 505, 'S'], [381, 201, 'T'], [360, 192, 'U'], [414, 313, 'V'], [525, 293, 'W'], [240, 563, 'X'],
        [117, 546, 'Y'], [507, 127, 'Z']]

# point = []
# points = {}
# for item in data:
#
#     x = item[0]
#     y = item[1]
#     key = str(item[2])
#     points[key] = [x, y]
#
# points.sort()
# key_list = points.keys()
# key = ""
# next_key = ""
#
# for i in range(len(key_list)):
#     key = key_list[i]
#     next_key = key_list[i+1]
#
# x1 = points[key][0]
# y1 = points[key][1]
# x2 = points[next_key][0]
# y2 = points[next_key][1]
# normx = x1-x2
# normy = y1 - y2
# distance = math.hypot(normx, normy)





#fixed
distance_A_dict = {}
point = []
points = {}
for item in data:

    x = item[0]
    y = item[1]
    key = str(item[2])
    points[key] = [x, y]

points.sort()
key_list = points.keys()
key = ""
next_key = ""

for i in range(len(key_list)):
    key = key_list[i+1]

x1 = points[key][0]
y1 = points[key][1]
x2 = points["A"][0]
y2 = points["A"][1]
normx = x1-x2
normy = y1 - y2
distancefromA = math.hypot(normx, normy)
distance_A_dict[key] = distancefromA


print distance_A_dict