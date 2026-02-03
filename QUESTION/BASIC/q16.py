n = int(input("Enter a number :"))

table = [n*i for i in range(1,11)]
# A=print(table)

with open ("table.txt","a") as f:
    f.write(f"The table of {n} is {str(table)}\n")

