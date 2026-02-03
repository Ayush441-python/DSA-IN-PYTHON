import random
n=random.randint(1,100)
a =-1
guesses = 0
while(a!=n):
    a = int(input("Guess the number: "))
    guesses+=1
    if(a>n):
        print("Lower number please")
    else:
        print("Higher number please")

print("YOU WIN U GUESS RIGHT NUMBER")
print(f"Number of guesses is {guesses} and Number is {n} ")