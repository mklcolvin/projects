def get_prime_numbers(numbers):
    # Define a helper function to check if a number is prime
    # A number n is prime if n >= 2 and it has no divisors between 2 and int(n**0.5) + 1
    def is_prime(n):
        # TODO: Return False if n is less than 2
        # TODO: Loop from 2 to int(n**0.5) + 1 and return False if any divisor divides n evenly
        # TODO: Return True if no divisors were found
        if n < 2:
            return False
        else:
            for i in (2, int(n**0.5)):
                if i % 2 == 0:
                    return False
            return True
 #       pass
    
    # Use filter() with the helper function to select prime numbers
    prime_numbers = filter(is_prime, numbers)
    
    # Return the list of selected prime numbers
    return list(prime_numbers)

my_numbers = [2,3,4,5,10,11,13,17,18,19]
print(get_prime_numbers(my_numbers))
