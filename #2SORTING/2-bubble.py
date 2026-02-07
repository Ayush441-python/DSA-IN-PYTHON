nums=[24,5,254,5,53,57,53,6,46,4,45]
n=len(nums)
for i in range(n):
    isSwap=False
    for j in range(n-i-1):
        if nums [j]>nums [j+1] :
        # swap
            temp = nums [j]
            nums [j] = nums [j+1]
            nums [j+1] = temp
            isSwap = True
    if not isSwap:
        break
print(nums)