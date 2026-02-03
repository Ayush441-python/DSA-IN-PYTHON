def conv_temp(celsius):
     x= f"The temp in Fahrenheit is {(9/5) * celsius + 32}"
     return x
temp = int(input("Enter the temp:"))
print(conv_temp(temp))