def is_pass(x):
    spc_char = ['@', '#', '&', '%']
    for i in range(len(x)):
        if x[i] in spc_char:
            return True
    return False
            
x = input("Enter the passward:")
Strong = is_pass(x)
if Strong:
        print("The passward is strong")
else:
        print("The passward is  not strong, try something new")
    