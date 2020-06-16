def multi_multiply(*factors):
    output = 1
    for factor in factors:
        output *= factor
    return output


def bulk_purchase(inventory, **purchase):
    for item in purchase:
        if item in inventory:
            inventory[item] += purchase[item]
        else:
            inventory[item] = purchase[item]


print multi_multiply(2, 2)
print multi_multiply(2, 2, 3, 5)

fruit = {
    'apples': 10,
    'oranges': 23
}

bulk_purchase(fruit, apples = 5, bananas = 15)

print fruit['apples']
