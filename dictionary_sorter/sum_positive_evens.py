def sum_positive_evens(numbers):
    # Write code here
    filter = [n for n in numbers if n % 2 == 0]
    strip_negatives = [n for n in filter if n > 0]
    even_positives = sum(abs(n) for n in strip_negatives)
    return even_positives

# Test cases
print(sum_positive_evens([2, 4, 6, 8, 10]))  # Output: 12
