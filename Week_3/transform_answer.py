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
expected = {
    73: [
        'Bob',
        'Student'
    ],
    123: [
        'Kevin',
        'Instructor'
    ]
}


def transform(input_list, key_field):
    output = {}
    for item in input_list:
        key_value = item[key_field]
        record = []
        fields = item.keys()
        for field_name in fields:
            if field_name is not key_field:
                field_value = item[field_name]
                record.append(field_value)
        output[key_value] = record
    return output

FIELD_KEY = "id"
result = transform(data, FIELD_KEY)
print(result)
print(result[123])