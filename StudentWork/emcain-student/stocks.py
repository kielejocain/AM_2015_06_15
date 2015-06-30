# GIVEN THE FOLLOWING LIST OF LIST
test_data = [
    ["2014-06-01", "APPL", 100.11], # could turn this into a set of objects. date, ticker(), float/currency
    ["2014-06-02", "APPL", 110.61],
    ["2014-06-03", "APPL", 120.22],
    ["2014-06-04", "APPL", 100.54],
    ["2014-06-01", "MSFT", 20.46],
    ["2014-06-02", "MSFT", 21.25],
    ["2014-06-03", "MSFT", 32.53],
    ["2014-06-04", "MSFT", 40.71],
]

# # CREATE TWO NEW LISTS ONE FOR EACH STOCK TICKER SYMBOL e.g. APPL and MSFT
#
#
#
# appl = []
# msft = []
#
# for item in test_data:
#     if item[1] == 'APPL':
#         appl.append(item)
#     else:
#         msft.append(item)
#
# print "appl"
# print appl
# print "msft"
# print msft
#
# # result example
#
# # appl = [
# #     ["2014-06-01", "APPL", 100.11],
# #     ["2014-06-02", "APPL", 110.61],
# #     ["2014-06-03", "APPL", 120.22],
# #     ["2014-06-04", "APPL", 100.54],
# # ]
# #
# # msft = [
# #     ["2014-06-01", "MSFT", 20.46],
# #     ["2014-06-02", "MSFT", 21.25],
# #     ["2014-06-03", "MSFT", 32.53],
# #     ["2014-06-04", "MSFT", 40.71],
# # ]
#
# print
# appl
# print
# msft
#
# # result example

# appl = [
#     ["2014-06-01", "APPL", 100.11],
#     ["2014-06-02", "APPL", 110.61],
#     ["2014-06-03", "APPL", 120.22],
#     ["2014-06-04", "APPL", 100.54],
# ]
#
# msft = [
#     ["2014-06-01", "MSFT", 20.46],
#     ["2014-06-02", "MSFT", 21.25],
#     ["2014-06-03", "MSFT", 32.53],
#     ["2014-06-04", "MSFT", 40.71],
# ]
#
# # Example Output to eliminate redundant data
#
# stocks = { #dict of... {'':[['','',''],[]], '':[[],[]]}
#     "appl": [ #string '' : list of... [['','',''],[]]
#         ["2014-06-01", "APPL", 100.11], #list of strings
#         ["2014-06-02", "APPL", 110.61],
#         ["2014-06-03", "APPL", 120.22],
#         ["2014-06-04", "APPL", 100.54],
#     ],
#     "msft": [
#         ["2014-06-01", "MSFT", 20.46],
#         ["2014-06-02", "MSFT", 21.25],
#         ["2014-06-03", "MSFT", 32.53],
#         ["2014-06-04", "MSFT", 40.71],
#     ]
# }



#ONCE THAT WORKS THEN what would need to change to copy with an unknown number of stock ticker symbols?


def categorize_stocks_list(stocks_list, corp_position=None, date_position=None, price_position=None): # input stocks_list = [['','',''],[]]
    if corp_position is None:
        corp_position = 1
    if date_position is None:
        date_position = 0
    if price_position is None:
        price_position = 2
    master_list = {}
    print "Making a dictionary of the stock prices...\n"
    for item in stocks_list: # item looks like this: ['','','']
        print 'item[' + str(corp_position) + '] is', item[corp_position]
        if item[corp_position] in master_list.keys(): # name of the company is in master_list
            print 'Company', item[corp_position], 'is in the dictionary, so we can add daily stock quotes to it.'
            master_list[item[corp_position]].append([item[date_position], item[price_position]])
        else:
            print "Company", item[corp_position], "is not in the dictionary. Let's add it!"
            # try adding extra crap from input on the end of the output lines.
            master_list[item[corp_position]] = [[item[date_position], item[price_position]]]

    return master_list # AAAAAAAAAAAAAAAAA THIS IS WHAT I WAS MISSING AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

def stocks_by_corp(the_dict):
    # 1. turn this string concatenation algorithm into list of lists, which is concatenated into a string in step 2
    # 2. sort. I could use a sort() type method but I want to experiment with putting them in the correct position as I add them.
    meta_list = [] # format [stockname, [[info, info][]],
    for blorp in the_dict:



    # for bloop in the_dict:
    #     output += 'listings for stock ' + bloop + ":\n" # this works.
    #     for the_list in the_dict[bloop]:
    #         output += str(the_list) + "\n"
    #         output += "this means that on date " + str(the_list[0]) + " the price of " + str(bloop) + " stock was " \
    #                   + str(the_list[1]) + "!\n"
    #     output += "Those were the prices for stock " + bloop + '!\n\n'

    output = ""
    # add the list items into a string
    return output

woo = categorize_stocks_list(test_data)
print "Raw dictionary:", woo
print "-"*10
print "Here is a better way of looking at this information. \n"
print stocks_by_corp(woo)

print 'Here is what the original data looks like now. '

print test_data
more_data = [
    ['BLOB', '2015-05-15', 20.45],
    ['BLEP', '2015-05-15', 10.33],
    ['BLOB', '2015-05-16', 21.04],
]

wee = categorize_stocks_list(more_data, 0, 1, 2)

print "here is the new stocks list, categorized"

print stocks_by_corp(wee)


#new task: sort the output somehow.