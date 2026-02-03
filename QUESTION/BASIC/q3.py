a=int((input("Enter the a:")))

rev=0
while(a>0):
    x=a%10
    rev=rev*10+x
    a=a//10

print(rev)
