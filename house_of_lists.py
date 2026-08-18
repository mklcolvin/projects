list_of_lists = [[1, 2], [3, 4], [5, 6]]
# Write code here
sublist = [sum(n) for n in list_of_lists if sum(n) < 50]
extracted_numbers = [item for item in sublist if item < 5]
flat = [num for inner in list_of_lists for num in inner if num in extracted_numbers]
print(flat)
# Output: [1, 2, 3, 4, 5, 6]