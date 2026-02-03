def pal(x):
    rev=x[::-1] 
    if x==rev:
        print("The string is palindrome")
    else:
        print("It is not")


x = input("Enter the string:")
pal(x)
