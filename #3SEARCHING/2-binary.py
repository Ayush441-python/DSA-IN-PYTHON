def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid+ 1
        else:
            high = mid- 1
        
    return -1
x = [1,2,3,5,6,7,9,7,5,3,56,89,5,4457,463,8,3278,54,4,75,45]
print(binary_search(x,56))



