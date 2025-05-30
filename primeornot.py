#Python program to check whether a given number is prime or not.

a=int(input("Enter a number "))
if a>1:
    for i in range(2,int(a/2)+1):
        if a%i==0:
            print("Not a Prime Number")
            break
    else:
        print("Prime Number")
else:
    print("Not a Prime Number")
