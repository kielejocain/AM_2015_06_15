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

list_dict = []
staff = {}
new_entries = []

for dict in data:
    new_key = dict["id"]
    new_entries.append(dict["name"])
    new_entries.append(dict["role"])

    staff[new_key] = new_entries


print staff

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

list_dict = []
staff = {}
new_entries = []

for dict in data:
    new_key = dict["id"]
    for entry in list_dict:
    new_entries = (dict["name"])
    staff[new_key] = new_entries


print staff


expected = {73: ['Bob', 'Student'], 123: ['Kevin', 'Instructor']}


def transform(input_list, key_field):
    output = {}
    # ... WORK
    return output


print(transform(data,"id"))
