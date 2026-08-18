def is_valid(username, password):
    if username == "user" or username == "admin":
        if username == "user" and password == "qweasd":
            return True
        
        if username == "admin":
            return True
        
    return False

myuser = input()
mypassword = input()
valid = is_valid(myuser, mypassword)
print(f'{valid}')
