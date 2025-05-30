#Python program to find factorial of a natural number using recursive function.

def fact (n):
    if n==1:
        return n
    else:
        return n*fact(n-1)
a=int(input("Enter a number"))
if a==0:
    print("Factorial is 1")
elif a<0:
    print("Enter a whole number ")
else:
    print("Factorial is ",fact(a))
