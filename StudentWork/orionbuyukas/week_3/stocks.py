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

# appl = []

appl = []
msft = []

for set in test_data:

    if "APPL" in set:
        appl.append(set)
    elif "MSFT" in set:
        msft.append(set)
print msft
print appl

# Example Output to ** eliminate ** redundant data
stocks = {}
apple = []
for dataset in appl:

    dataset.remove("APPL")
    apple.append(dataset)
    stocks["appl"] = apple


microsoft = []
for dataset in msft:
    dataset.remove("MSFT")
    microsoft.append(dataset)
    stocks["msft"] = microsoft

print stocks


def stock_dict(stock_symbol, stock_name):
    stock_name=[]
    for dataset in stock_symbol:
        dataset.remove(stock_symbol)
        stock_name.append(dataset)
        stocks[stock_symbol] = stock_name


def list_to_dict(test_data):
    field_position_index =1
    output_dict = {}
    for row in test_data = row[field_position_index]:
        keys = output_dict.keys()
        if column_value not in keys:
            output_dict[column_value] = [] #empty list to be added to
        list = output_dict[column_value]
        #row.pop(field_position_index)
        #item = [row[0], row[2]]
        item = []
        for f in range(0, len(row+1)): # creates a list with eveything but key field
            if f == field_position_index:
                pass
            else:
                item.append(row[f])
        list.append(item)
    return output_dict

