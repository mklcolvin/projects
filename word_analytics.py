def analyze_text(text):

    import re
    from collections import Counter

    # Your solution here
    
    # 1. Split the text into words and normalize them
    # (make lowercase and remove punctuation)

    # make all words lowercase
    lowercase_text = text.lower()

    # remove all punctuation
    cleaned_text = re.sub(r'[^\w\s]', '', lowercase_text)
    # print(cleaned_text)

    # Set the counters for frequencies of words
    unique_words = 0
    repeated_words = 0
    repeated_words_list = []
    palindromes_list = []

    # 2. Count the occurrences of each word
    words = cleaned_text.split()
    freq = Counter(words)
    unique_words = len(freq)

    # 3. Find the number of unique words
    # 4. Identify repeated words (appearing more than once)

    for w, c in freq.items():
#        print(w, ":", c)
        if c > 1:
            repeated_words += 1
            repeated_words_list.append(w)

        # Check to see if it is a palindrome
        # 5. Find palindrome words
        if w == w[::-1]:
            palindromes_list.append(w)
    

    print(f"Unique words: {unique_words}    Repeated words: {repeated_words}")

    repeated_words_list.sort()
    palindromes_list.sort()
    

    
    # 6. Return the results in a dictionary with sorted lists
    
    my_dictionary = {"unique count": unique_words, "repeated words": repeated_words_list, "palindromes": palindromes_list}
    print(my_dictionary)


input = "Wow! Did Hannah see that Race car? Mom was there too. Hannah did see it!"
output = analyze_text(input)