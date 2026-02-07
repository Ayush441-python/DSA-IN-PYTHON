# def linear_search(arr, target):
#     for i in range(len(arr)):
#         if arr[i] == target:
#             return i   # element found at index i
#     return -1          # element not found

def lin_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return print(f"The index of the target is {i}")
    return print("BKL sahi number dal") 


x = [1,2,3,5,6,7,9,7,5,3,56,89,5,4457,463,8,3278,54,4,75,45]
lin_search(x,4457)

