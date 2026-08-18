# Write code here
try:
    number = int(input())
    print(f"You entered: {number}")
except TypeError:
    print("Invalid input! Please enter a valid number.")
