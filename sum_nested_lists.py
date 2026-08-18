def sum_nested(nested_list):
    total = 0
    for element in nested_list:
        if isinstance(element, list):  # Check if the element is a list
            # TODO: Recursively call sum_nested on the sublist and add to total
            total += sum_nested(element)
        else:
            # TODO: Add the integer directly to total
            total += element
    return total


result = sum_nested([1, [2, 3], [4, [5, 6]], 7])
print(result)  # Output should be 28
