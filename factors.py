#Python program to print the factors of a given number.

a=int(input("Enter a number "))
print("The factors are ")
for i in range(1,a+1):
     if a%i==0:
         print(i)
