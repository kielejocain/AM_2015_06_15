data = [
    {
        "id": 123,
        "name": "Kevin",
        "role": "Instructor"
    },
    {
        "id": 73,
        "name": "Bob",
        "role": "Student"
    }
]

## loopless solution
# result = {
#     data[0]["id"]: [data[0]["name"], data[0]["role"]],
#     data[1]["id"]: [data[1]["name"], data[1]["role"]],
# }
# print(result)
expected = {73: ['Bob', 'Student'], 123: ['Kevin', 'Instructor']}


def transform(input_list, key_field):
    output = {}
    for entry_dict in input_list:
        current_key = entry_dict[key_field]
        current_value = [entry_dict["name"], entry_dict["role"]]
        output[current_key] = current_value
    return output

print(transform(data,"id"))

