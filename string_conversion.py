numbers = input()
prefix = input()
nums = numbers.split()
result_nums  = []
for num in nums:
    result_nums .append(prefix + num)
result = ' '.join(result_nums)
print(result)