nums=[24,5,254,5,53,57,53,6,46,4,45]
n = len(nums)
for i in range(1,n):
    key = nums[i]
    j = i-1
    while j>=0 and nums[j]>key:
        nums[j+1]=nums[j]
        j-=1
    nums[j+1]=key
print(nums)     