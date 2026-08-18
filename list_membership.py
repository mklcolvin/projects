lst1 = input().split(",")
lst2 = input().split(",")
lst3 = []
# Write your code below
for i in range(len(lst1)):
    if lst1[i] not in lst2:
        lst3.append(lst1[i])
print(lst3)
