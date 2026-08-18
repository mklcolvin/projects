def sum_digits(n):
    # Write code here
    if n < 10:
        return n
    else:
        converted_number_to_string = str(n)
        last_digit = int(converted_number_to_string[-1])
        result = last_digit + sum_digits(n // 10)
        return result


test_result = sum_digits(555)
print(test_result)   # Output: 15