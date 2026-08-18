mynumber = int(input())
factorial = 1
for i in range(2, mynumber + 1):
    factorial *= i
print(f'factorial = {factorial}')