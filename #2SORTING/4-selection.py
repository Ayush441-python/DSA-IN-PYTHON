nums=[24,5,254,5,53,57,53,6,46,4,45]

n = len(nums)
for i in range(n):
    mn = nums[i]
    ind = i
    for j in range(i+1,n):
        if nums[j]<mn:
            mn = nums[j]
            ind = j
    temp = nums [i]
    nums [i] = nums [ind]
    nums [ind] = temp
print(nums )