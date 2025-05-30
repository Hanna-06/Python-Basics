#Python program to check if a number is palindrome or not.

a=int(input("Enter a number "))
temp=a
rev=0
while(a>0):
    n=a%10
    rev=rev*10+n
    a=a//10
if temp==rev:
    print("Palindrome")
else:
    print("Not a Palindrome")
