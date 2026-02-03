a=int((input("Enter the a:")))
orig =a
rev=0
while(a>0):
    x=a%10
    rev=rev*10+x
    a=a//10
print(rev)
if(rev==orig):
    print("palindrome",bool(rev==orig))
else:
    print(False)