import numbers

def multiply_by_two(x):
    return x * 2

def multiply_by_three(x):
    return x * 3

def build_list(items):
    new_list = []
    for item in items:
        if item % 2 == 0:
            new_list.append(multiply_by_two(item))
        else:
            new_list.append(multiply_by_three(item))
    return new_list


def process_numbers(numbers):
    # Write your code below
    numbers_filter = filter(lambda first: first > 0, numbers) 
    num_filter_list = list(numbers_filter)
    return build_list(num_filter_list) 

mylist = [-4, 0, 5, 2, 8, -3, 7]
processed_list = process_numbers(mylist)