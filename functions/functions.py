def sums():
    total = 0
    for mysum in range(1, 10001):
        total += mysum
    print(f'{total}')

mycount = int(input())
for i in range(mycount):
    sums()
