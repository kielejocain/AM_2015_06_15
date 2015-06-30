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

print appl
print msft

#ONCE THAT WORKS THEN what would need to change to copy with an unknown number of stock ticker symbols?