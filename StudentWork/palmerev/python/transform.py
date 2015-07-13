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
    for item in input_list:
        new_key = item[key_field]
        output[new_key] = []
        for key, value in item.items():
            if value != new_key: # don't copy redundant field
                output[new_key].append(value)
    return output


print(transform(data,"id"))
