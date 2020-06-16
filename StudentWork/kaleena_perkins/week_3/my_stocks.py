# # GIVEN THE FOLLOWING LIST OF LIST
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
#
# # CREATE TWO NEW LISTS ONE FOR EACH STOCK TICKER SYMBOL e.g. APPL and MSFT
#
appl = []
msft = []

def stocks(lst):
	for item in test_data:
		if "APPL" in item:
			appl.append(item)
		elif "MSFT" in item:
			msft.append(item)
	return msft, appl


stocks(test_data)
print appl
print msft
#
# # result example
#
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
def remove_data(lst):
    for i in lst:
        if i[1] == ("APPL" or 'MSFT'):
            del i[1]
    return lst

print remove_data(appl)
print remove_data(msft)

stocks = {"appl": [],
          "msft": []}
def stock_dict(lst):
    for i in lst:
        if "APPL" in i:
            stocks["appl"].append(i)
        elif "MSFT" in i:
            stocks["msft"].append(i)


print stock_dict(test_data)

# def list_to_dict(test_data):
#     FIELD_POSITION_INDEX = 1
#     output_dict = {}
#     for row in test_data:
#         column_value = row[FIELD_POSITION_INDEX]
#         keys = output_dict.keys()
#         if column_value not in keys:
#             output_dict[column_value] = []
#         list = output_dict[column_value]
#         row.pop(FIELD_POSITION_INDEX)
#         list.append(row)
#     return output_dict
#
#
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



#ONCE THAT WORKS THEN what would need to change to copy with an unknown number of stock ticker symbols?
