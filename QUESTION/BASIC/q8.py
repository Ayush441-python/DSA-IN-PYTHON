import math
def fact(n):
    if(n==1 or n==0):
        return 1
    else:
        return n*fact(n-1)
a=int((input("Enter the number for find factorial:")))
x=fact(a)
print(x)


