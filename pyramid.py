n = int(input())    
value = "*"
number_of_rows = (n + 1) // 2
for i in range(0, number_of_rows):
    print(value)
    value +=  "**"

