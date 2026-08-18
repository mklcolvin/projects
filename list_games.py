numbers = input().split()
# Write your code below
original_list = numbers.copy()
temp_list = numbers.copy()
temp_list.reverse()
for i in range(len(numbers)):
    numbers.append(temp_list[i])
numbers.insert(0, original_list[0])
numbers.append(original_list[-1])
new_list = numbers.copy()
for i in range(len(numbers)):
    numbers.append(numbers[i])

for i in range(len(new_list)):
    numbers.append(new_list[i])

print(numbers)
