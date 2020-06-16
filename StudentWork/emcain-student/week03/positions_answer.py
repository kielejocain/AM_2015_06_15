from math import sqrt, hypot # we will be using these for two different methods of the
from string import lowercase, uppercase  # adding this


# data is  a list of lists, each of which contains the x coord, y coord and letter.
data = [[531, 408, 'A'], [225, 52, 'B'], [594, 242, 'C'], [351, 102, 'D'], [371, 15, 'E'], [569, 353, 'F'],
        [342, 39, 'G'], [218, 304, 'H'], [428, 260, 'I'], [329, 158, 'J'], [585, 530, 'K'], [71, 114, 'L'],
        [587, 88, 'M'], [347, 180, 'N'], [180, 332, 'O'], [250, 522, 'P'], [88, 475, 'Q'], [260, 128, 'R'],
        [328, 505, 'S'], [381, 201, 'T'], [360, 192, 'U'], [414, 313, 'V'], [525, 293, 'W'], [240, 563, 'X'],
        [117, 546, 'Y'], [507, 127, 'Z']]
square_size = 610   # defines a variable which will be used to create the square
                    # the above points live in
# define html style
style = """
<style>
    #box { background:blue; position:relative; }
    #box span { color:silver; position:absolute; }
</style>
"""


def distance(p1, p2): # 2 alternate ways of calculating distance btwn 2 points
    # return (sqrt( (p2[0] - p1[0])**2 + (p2[1] - p1[1])**2 ))
    return (hypot(p2[0] - p1[0], p2[1] - p1[1]))


letter_dict = {}
for d in data:
    letter = d[2]  # makes the letter in the sublist in data into the key in this dict
    letter_dict[ letter ] = d  # assigns the value to key letter as the full sublist.
                                    # this creates some redundancy, last value not needed
                                    # I added the range to d

#print letter_dict

# for arbitrary value e.g. "J" find the nearest N items e.g. 5
def get_top(data, letter, top_n):
    selected = letter_dict[letter]
    # Calculate distance and append as 4th element after lat, long, and letter
    for v in data:
        dist = distance(v, selected)
        v.append(dist)

    s = sorted(data, key=lambda item: item[3]) # sort on distance
    return s[1:top_n + 1]


top = get_top(data, "V", 5) # this does not return items of the same  type as those in data so the color change funtion is not working

# print "top as gt:", top_as_gt
#
# # convert top_as_gt back into data type form
#
# top_letters = []
# for item in top_as_gt:
#     top_letters.append(item[2])
#
# print "top letters: ", top_letters
#
# top = []
#
# for item in data:
#     if item[2] in top_letters:
#         top.append(item)

print "top", top

f = open("positions.html", "w")
f.write(style)
f.write('<div id="box" style="width:{0}px;height:{0}px;">\n'.format(square_size))
for item in data:
    if item in top:
        c = "color:red; " #not working for some reason.
        print "item", item, "is in top\n"
    elif item == data[-5]: # I think the issue is that this needed to be an elif instead of an if
        c = "color:green; "
        print "item", item, "is the search key\n"
    else:
        c = ""
        print "item", item, "is not highlighted\n"
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

#CLUES - Ways of calculating distance between two points.
# dist = sqrt( (x2 - x1)**2 + (y2 - y1)**2 )
# dist = math.h