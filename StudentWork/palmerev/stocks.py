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

appl = [test_data[i] for i in range(4)]
msft = [test_data[i] for i in range(4, 8)]
#
print "appl:",appl
print "msft:",msft

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

# Example Output to eliminate redundant data

stocks = {
    "appl": [
        ["2014-06-01", "APPL", 100.11],
        ["2014-06-02", "APPL", 110.61],
        ["2014-06-03", "APPL", 120.22],
        ["2014-06-04", "APPL", 100.54],
    ],
    "msft": [
        ["2014-06-01", "MSFT", 20.46],
        ["2014-06-02", "MSFT", 21.25],
        ["2014-06-03", "MSFT", 32.53],
        ["2014-06-04", "MSFT", 40.71],
    ]
}

print stocks

stocks2 = list(stocks)
#ONCE THAT WORKS THEN what would need to change to copy with an unknown number of stock ticker symbols?
print 2 * "\n"

for stock, tickets in stocks.items():
    for ticket in tickets:
        del ticket[1]

print stocks

from collections import defaultdict
def list_to_dict(stock_list, key_field_index=None):
    stock_dict = defaultdict(list)
    for ticket in stock_list:
        if key_field_index < 0 or key_field_index > len(ticket):
            print "invalid field to remove."
        #stock_name = ticket[1]
        key_field = ticket[key_field_index]
        ticket_fields = []
        for i, field in enumerate(ticket):
            if i != key_field_index:
                ticket_fields.append(field)
        stock_dict[key_field].append(ticket_fields)
    return stock_dict

st = list_to_dict(test_data, 1)

print st
print test_data
