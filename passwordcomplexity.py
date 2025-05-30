#Python program to check the complexity of a password.

import re
def password(pw):
    if len(pw)<B:
        return False
    if not re.search(r'[A-Z]',pw):
        return False
    if not re.search(r'[a-z]',pw):
        return False
    if not re.search(r'\d',pw):
        return False
    if not re.search(r'[!@#$%^&*()_-=+]',pw):
        return False
    else:
        return True
pw=input("Enter password")
valid password(pw)
if valid:
    print("Password is strong")
else:
    print("Password is weak")
