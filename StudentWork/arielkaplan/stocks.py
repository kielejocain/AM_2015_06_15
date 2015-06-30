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

def sort_stocks_by_name():
    stocks = {}

    for entry in test_data:
        # create key from entry[1]
        current_stock = entry[1].lower()
        if current_stock not in stocks:
            stocks[current_stock] = []
        # remove stock name from entry to eliminate redundant data
        mod_entry = [entry[0], entry[2]]
        stocks[current_stock].append(mod_entry)

    for key in stocks.keys():
        print key
        for list in stocks[key]:
            print list

# sort_stocks_by_name()

# EXTRA CREDIT: Take as a parameter which field to use as the id

def sort_stocks(id): # id is 0, 1, 2 for index of list
    stocks = {}
    for entry in test_data:
        # create key from entry[id], lowercase if possible
        try:
            current_stock = entry[id].lower()
        except:
            current_stock = entry[id]

        # set value to empty list if key not there
        if current_stock not in stocks:
            stocks[current_stock] = []
        # remove stock name from entry to eliminate redundant data
        mod_entry = entry[:]
        del mod_entry[id]
        stocks[current_stock].append(mod_entry)

    for key in stocks.keys():
        print key
        for list in stocks[key]:
            print list

sort_stocks(0)
sort_stocks(1)
sort_stocks(2)