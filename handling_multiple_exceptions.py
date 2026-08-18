def process_data(input_string):
    try:
        # Try to convert the input string to an integer
        input = int(input_string)
        # Calculate 100 divided by the input value
        result = 100 / input
        # Return the result
        return result
    except ValueError:
        # Handle the case where input cannot be converted to an integer
        print("Input must be a number!")
    except ZeroDivisionError:
        # Handle the case where input is zero
        print("Cannot divide by zero!")
    except:
        # Handle any other unexpected exceptions
        print("An unexpected error occured!")
        
    return None

# Example usage
print(process_data("10"))  # Should print 10.0
print(process_data("0"))   # Should print "Cannot divide by zero!"
