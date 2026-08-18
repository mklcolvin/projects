def dictionary_sorter(data_dict):
    # Use sorted() to sort the dictionary items by their values
    # Hint: data_dict.items() returns (key, value) pairs
    # Hint: Use the 'key' parameter of sorted() to sort by value

    # Write code here
    sorted_items = sorted(data_dict.items(), key=lambda item: item[1])
    sorted_dict = {key: value for key, value in sorted_items}
    return sorted_dict