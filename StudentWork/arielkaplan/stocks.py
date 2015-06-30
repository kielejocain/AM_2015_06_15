# GIVEN THE FOLLOWING LIST OF LIST
test_data = [
    ["2014-06-01", "APPL", 100.11],
    ["2014-06-02", "APPL", 110.61],
    ["2014-06-03", "APPL", 120.22],
    ["2014-06-04", "APPL", 100.54],
    ["2014-06-01", "MSFT", 20.46],
    ["2014-06-02", "MSFT", 21.25],
    ["2014-06-03", "MSFT", 32.53],
    ["2014-06-04", "MSFT", 40.71],
]

# CREATE TWO NEW LISTS ONE FOR EACH STOCK TICKER SYMBOL e.g. APPL and MSFT

appl = []
msft = []

for entry in test_data:
    if entry[1] == "APPL":
        appl.append(entry)
    elif entry[1] == "MSFT":
        msft.append(entry)
    else:
        print 'Error'

# result example

appl = [
    ["2014-06-01", "APPL", 100.11],
    ["2014-06-02", "APPL", 110.61],
    ["2014-06-03", "APPL", 120.22],
    ["2014-06-04", "APPL", 100.54],
]

msft = [
    ["2014-06-01", "MSFT", 20.46],
    ["2014-06-02", "MSFT", 21.25],
    ["2014-06-03", "MSFT", 32.53],
    ["2014-06-04", "MSFT", 40.71],
]

print appl
print msft

stocks = {}

stocks[appl[0][1].lower()] = appl
stocks[msft[0][1].lower()] = msft

# print stocks

# result example

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

# Example Output to eliminate redundant data

# stocks = {
#     "appl": [
#         ["2014-06-01", "APPL", 100.11],
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



#ONCE THAT WORKS THEN what would need to change to copy with an unknown number
# of stock ticker symbols?

def sort_stocks_by_name(test_data):
    stocks = {}

    for entry in test_data:
        # add field position index so don't have "magic variable"
        # i.e. random number with no context
        FIELD_POS_INDEX = 1
        # create key from entry[FIELD_POS_INDEX]
        current_stock = entry[FIELD_POS_INDEX].lower()
        if current_stock not in stocks:
            stocks[current_stock] = []
        # remove stock name from entry to eliminate redundant data
        mod_entry = [entry[0], entry[2]]
        stocks[current_stock].append(mod_entry)

    for key in stocks.keys():
        print key
        for list in stocks[key]:
            print list

# sort_stocks_by_name(test_data)

# EXTRA CREDIT: Take as a parameter which field to use as the id

def sort_stocks(test_data, FIELD_POS_INDEX): # 0, 1, 2 for index of list
    stocks = {}
    for entry in test_data:
        # create key from entry[FIELD_POS_INDEX], lowercase if possible
        try:
            current_stock = entry[FIELD_POS_INDEX].lower()
        except:
            current_stock = entry[FIELD_POS_INDEX]

        # set value to empty list if key not there
        if current_stock not in stocks: # or stocks.keys()
            stocks[current_stock] = []

        # remove stock name from entry to eliminate redundant data
        mod_entry = entry[:] # copy list to not mod original
        del mod_entry[FIELD_POS_INDEX]
        stocks[current_stock].append(mod_entry)

    for key in stocks.keys():
        print key
        for list in stocks[key]:
            print list

sort_stocks(test_data, 0)
sort_stocks(test_data, 1)
sort_stocks(test_data, 2)

# EXTRA CREDIT: All objects rather than list??