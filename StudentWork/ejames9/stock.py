
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


appl = []
msft = []

for i in test_data:
   if "APPL" in i:
       appl.append(i)
   elif "MSFT" in i:
       msft.append(i)
#
# print appl
# print msft

stocks = {}
for entry in test_data:
    ticker = entry[1]
    if ticker not in stocks:
        stocks[ticker] = []
    stocks[ticker].append(entry)


# for entry in appl:
#     stocks['APPL'].append(entry)
# for entry in msft:
#     stocks['MSFT'].append(entry)
for symbol in stocks:
    print symbol
    for item in stocks[symbol]:
        print item

print stocks
