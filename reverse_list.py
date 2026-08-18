def reverse(lst):
    # Write code here
    lst2 = [0] * len(lst)
    for i in range(len(lst), 0, -1):
        test = len(lst) - i
        lst2[i - 1] = lst[test]

    return lst2

lst = [1, 2, 3, 4, 5]
print(reverse(lst))