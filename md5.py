#Python program to implement MD5 hash.

import hashlib
str=input("Enter a string: ")
a=hashlib.md5(str.encode())
print("The MD5 hash is: ")
print(a.hexdigest())
print("The byte equivalent is: ")
print(a.digest())
