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

APPL = []
MSFT = []

for row in test_data:
    ticker_symbol = row[1]
    if ticker_symbol == "APPL":
        APPL.append(row)
    elif ticker_symbol == "MSFT":
        MSFT.append(row)
print(APPL)
print(MSFT)

# result example

APPL = [
    ["2014-06-01", "APPL", 100.11],
    ["2014-06-02", "APPL", 110.61],
    ["2014-06-03", "APPL", 120.22],
    ["2014-06-04", "APPL", 100.54],
]

MSFT = [
    ["2014-06-01", "MSFT", 20.46],
    ["2014-06-02", "MSFT", 21.25],
    ["2014-06-03", "MSFT", 32.53],
    ["2014-06-04", "MSFT", 40.71],
]

# print(APPL)
# print(MSFT)

# result example

APPL = [
    ["2014-06-01", "APPL", 100.11],
    ["2014-06-02", "APPL", 110.61],
    ["2014-06-03", "APPL", 120.22],
    ["2014-06-04", "APPL", 100.54],
]

MSFT = [
    ["2014-06-01", "MSFT", 20.46],
    ["2014-06-02", "MSFT", 21.25],
    ["2014-06-03", "MSFT", 32.53],
    ["2014-06-04", "MSFT", 40.71],
]

# Example Output to eliminate redundant data

stocks = {
    "APPL": [
        ["2014-06-01", "APPL", 100.11],
        ["2014-06-02", "APPL", 110.61],
        ["2014-06-03", "APPL", 120.22],
        ["2014-06-04", "APPL", 100.54],
    ],
    "MSFT": [
        ["2014-06-01", "MSFT", 20.46],
        ["2014-06-02", "MSFT", 21.25],
        ["2014-06-03", "MSFT", 32.53],
        ["2014-06-04", "MSFT", 40.71],
    ]
}

stocks = {
    "APPL": [
        ["2014-06-01", 100.11],
        ["2014-06-02", 110.61],
        ["2014-06-03", 120.22],
        ["2014-06-04", 100.54],
    ],
    "MSFT": [
        ["2014-06-01", 20.46],
        ["2014-06-02", 21.25],
        ["2014-06-03", 32.53],
        ["2014-06-04", 40.71],
    ]
}



# ONCE THAT WORKS THEN what would need to change to copy with an unknown number of stock ticker symbols?
def list_to_dict(test_data):
    FIELD_POSITION_INDEX = 1
    output_dict = {}
    for row in test_data:
        column_value = row[FIELD_POSITION_INDEX]
        keys = output_dict.keys()
        if column_value not in keys:
            output_dict[column_value] = []
        list = output_dict[column_value]
        row.pop(FIELD_POSITION_INDEX)
        list.append(row)
    return output_dict


result = list_to_dict(test_data)
print(result)
print(test_data)