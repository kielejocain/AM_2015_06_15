from math import sqrt

Latitude = 0
Longitude = 1
Letter = 2

location_list = [[531, 408, 'A'], [225, 52, 'B'], [594, 242, 'C'], [351, 102, 'D'], [371, 15, 'E'], [569, 353, 'F'],
        [342, 39, 'G'], [218, 304, 'H'], [428, 260, 'I'], [329, 158, 'J'], [585, 530, 'K'], [71, 114, 'L'],
        [587, 88, 'M'], [347, 180, 'N'], [180, 332, 'O'], [250, 522, 'P'], [88, 475, 'Q'], [260, 128, 'R'],
        [328, 505, 'S'], [381, 201, 'T'], [360, 192, 'U'], [414, 313, 'V'], [525, 293, 'W'], [240, 563, 'X'],
        [117, 546, 'Y'], [507, 127, 'Z']]

# def calculateDistance(x1,y1,x2,y2):
#     dist = math.sqrt((x2-x1)**2 + (y2-y1)**2)
#     return dist

def distance(point_from, point_to):
    lateral_distance = point_from[Latitude] - point_from[Latitude]
    longitudinal_distance = point_to[Longitude] - point_to[Longitude]
    return sqrt(lateral_distance **2 + longitudinal_distance **2)

letter_dictionary = {}
for location in location_list:
    letter = location(2)
    letter_dictionary[letter] = location

def get_top(data, letter, top_n):
    selected = letter_dictionary[letter]

    for location in data:
        dist = distance(location, selected)
        location.append(dist)

    s = sorted(location_list, key = lambda item:item[3])
    return s[0:top_n + 1]


output = []
top = get_top(location_list, "N", 5)
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









# for item in data:
#     letter = item[2]
#     x = item[0]
#     y = item[1]
#     letter_dictionary = [x,y]
#
# print letter_dictionary
# import math
#
# def new_dictionary(data):
#     capital_letter = 2
#     alphabet = {}
#
#     for alpha in data:
#         column_value = alpha[capital_letter]
#         key = alphabet.keys()
#
#         if column_value not in key:
#             alphabet[column_value] = []
#         list = alphabet[column_value]
#         alpha.pop(capital_letter)
#         list.append(alpha)
#
#     else:
#         return alphabet
#
# result = new_dictionary(data)
# print result
#
#
# def locations(alphabet):
#     x = 0
#     y = 1
#
# def calculateDistance(x1,y1,x2,y2):
#     dist = math.sqrt((x2-x1)**2 + (y2-y1)**2)
#     return dist
#
# distance = calculateDistance(3,5,5,7)
# print distance



#CLUES - Ways of calculating distance between two points.
# dist = sqrt( (x2 - x1)**2 + (y2 - y1)**2 )
# dist = math.hypot(x2 - x1, y2 - y1)



