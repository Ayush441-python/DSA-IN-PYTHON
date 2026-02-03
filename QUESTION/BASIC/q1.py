a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
c=int(input("Enter the value of c:"))


if(a==c):
    print("Error")
else:
    x=((a + b) ** 2 - (b + c) ** 2) / (a - c)
    print(f"The result of expression is {x}")

