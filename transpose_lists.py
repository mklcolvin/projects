def transpose(lst):
    if not lst:
        return []
        
    row_len = len(lst[0])
    col_len = len(lst)
    lst2 = [[0 for i in range(col_len)] for j in range(row_len)]
    for i in range(row_len):
        for j in range(col_len):
            lst2[i][j] = lst[j][i]  
    return lst2 



my_lst = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(f'my_lst: {my_lst}')
# Output: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
print(f'transposed: {transpose(my_lst)}')
