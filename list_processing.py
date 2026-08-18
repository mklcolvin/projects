input_list = input().split(', ')
# Write your code below
result = []
if len(input_list) >= 5:
    result = input_list[0:2]
    result.append(input_list[len(input_list) - 2 ])
    result.append(input_list[len(input_list) - 1 ])
else:
    result = input_list[0:1]
    result.append(input_list[len(input_list) - 1 ])
print(result)