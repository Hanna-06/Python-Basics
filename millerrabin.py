#Python program to implement primality testing using Miller-Rabin method.

def factorise(n):
    result=[0,0]
    while n%2==0:
        n/=2
        result[0]+=1
    result[1]=int(n)
    return result

def miller_rabin(n,b):
    [k,m]=factorise(n-1)
    if n==2:
        return True
    if(b**m)%n==1 or (b**m)%n==n-1:
        return True
    else:
        for i in range(10):
            if(b**(m*2**i))%n==1:
                return False
            elif (b**(m*2**i))%n==n-1:
                return True
    return False

n=int(input("Enter a number to test: "))
b=int(input("Enter a base to test against: "))
if miller_rabin(n,b):
    print (f"{n} is a probable prime")
else:
    print(f"{n} is a composite number")
