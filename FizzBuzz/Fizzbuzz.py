print("Welcome to FizzBuzz!")
def fizzbuzz (number):
    if (number % 3 == 0) or (number % 7 == 0):
        if (number % 3 == 0) and (number % 7 != 0):
            return "Fizz"
        if (number % 7 == 0) and (number % 3 != 0):
            return "Buzz"
        if (number % 3 == 0) and (number % 7 == 0):
            return "FizzBuzz"
    

    else:        
        return str(number)

    


number = int(input())
for i in range (1, number + 1):
    result = fizzbuzz(i)
    if ("3" in str(i)) and (i % 3 != 0) and (i % 7 != 0):
        print("Almost Fizz")
    else:
        print(f"{result}")
    