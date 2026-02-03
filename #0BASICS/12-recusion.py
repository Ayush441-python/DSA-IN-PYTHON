# def PrintNO(i,x):

#     if i>x :
#         return
#     print(i)
#     PrintNO(i+1,x)
# x = int(input("Enter the number :"))
# i = int(input("Enter the starting number :"))
# PrintNO(i,x)


# def Fact(n):
    
#     if n==0: 
#         return 1
#     return n*Fact(n-1)
    
# n = int(input("Enter the number :"))
# print(Fact(n))


def Fib(n):
    if n==1 :
        return 1 
    if n==0 :
        return 0 
    return Fib(n-1) + Fib(n-2)


n = int(input("Ente the number :"))
print(Fib(n))
