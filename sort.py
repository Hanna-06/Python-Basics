#Python program to read a list of numbers, sort the list in non-decreasing order without using built in functions. Separate function is written to sort the list where the name of the list is passed as parameter.

def sort(list,a):
    for i in range(0,a):
        for j in range(i+1,a):
            if list[i]>=list[j]:
                list[i],list[j]=list[j],list[i]
    print("The sorted list is ",list)
list=[]
a=int(input("Enter the number of elements of list "))
print("Enter the elements ")
for i in range(0,a):
    element=int(input())
    list.append(element)
print("The list before sorting ",list)
sort(list,a)
