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


def transform(input_list):
    output = {}
    for item in data:
        output[item['id']] = [item['name'], item['role']]
    return output


print(transform(data))
