def find_occurrences(text, pattern):
    # Write your code here
    occurrences = []
    match_found = False
    matches = 0
    pattern_length = len(pattern)
    if pattern in text:
        for i in range(len(text) - pattern_length + 1):
            if text[i:i + pattern_length] == pattern:
                occurrences.append(i)
                matches += 1
                match_found = True
    
    return [match_found, matches, occurrences]



# Read input
text = input()
pattern = input()

# Call your function and print the result
result = find_occurrences(text, pattern)
print(result)