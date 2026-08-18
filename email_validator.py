def clean_email_list(emails):
    # Write your code below
    stripped_strings_map = map(lambda x: x.strip(), emails)
    stripped_strings = list(stripped_strings_map)
 #   print("stripped_strings:", list(stripped_strings))
    lowercase_strings_map = map(lambda word: word.lower(), stripped_strings)
    lowercase_strings = list(lowercase_strings_map)
#  print("lowercase_strings:", list(lowercase_strings))
    one_at_strings_filter = filter(lambda tested: tested.count("@") == 1, lowercase_strings)
    one_at_strings = list(one_at_strings_filter)
#   print("one_at_strings:", list(one_at_strings))   
    # Split each string into a username and a domain
    valid_emails = filter(lambda x: not x.startswith('@') and not x.endswith('@'), one_at_strings)
    valid_emails_list = list(valid_emails)
#   print("valid_emails:", valid_emails)
    return list(valid_emails)

list_of_emails = ["Test@EXAMPLE.com",  "invalid.email",  "user@domain@.com",   "space@email.com"  ,  "valid@domain.com"]
print(clean_email_list(list_of_emails))