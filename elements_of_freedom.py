def elements_of_freedom(elements):
    # Your solution here
    
    # Step 1: Filter elements with length >= 5
    filtered_lists = [lst for lst in elements if len(lst) >= 5]
    # Step 2: Convert filtered elements to uppercase
    converted_list = [x.upper() for x in filtered_lists]
    # Step 3: Create a list of unique elements
    seen = set()
    unique_elements = [x for x in converted_list if not (x in seen or seen.add(x))]
    # Step 4: Return the final result
    return unique_elements

input_data = ["freedom", "liberty", "justice", "hope", "dreams", "hope", "peace"]
result = elements_of_freedom(input_data)
print(result)
