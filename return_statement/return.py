iterations = int(input())
num1 = int(input())
num2 = int(input())

def bigger(arg1, arg2):
    if arg1 > arg2:
       return arg1

    if arg2 > arg1:
        return arg2

    if arg1 == arg2:
        return arg1
    

    

for i in range(iterations):
    result = bigger(num1, num2)

    if result == num1:
        num1 = result / 2
        result = num1
    if result == num2:
        num2 = result / 2
        result = num2

    print(f'{result}')
        
    if result < 2:
        break

