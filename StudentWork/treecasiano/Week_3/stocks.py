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
for stock in test_data:
    if stock[1] == "APPL":
        del stock[1]
        appl.append(stock)
    if stock[1] == "MSFT":
        del stock[1]
        msft.append(stock)

print "appl: ", appl
print "msft: ", msft

# ONCE THAT WORKS THEN what would need to change
# to copy with an unknown number of stock ticker symbols?

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


def list_to_dict(test_data):
    stocks = {}
    FIELD_POSITION_INDEX = 1
    for stock in test_data:
        column_value = stock[FIELD_POSITION_INDEX]
        keys = stocks.keys()
        if column_value not in keys:
            stocks[column_value] = []
        list = stocks[column_value]
        stock.pop(FIELD_POSITION_INDEX)
        list.append(stock)
    return stocks

result = list_to_dict(test_data)

print(result)
print(test_data)
