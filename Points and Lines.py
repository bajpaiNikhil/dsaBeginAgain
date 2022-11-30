
nums = [9,5,7,8,7,9,8,2,0,7]
nums.sort()
print(nums)

left = 0
right = len(nums)-1
average = []
while left<right:
    average.append((nums[left]+nums[right])/2)
    left+=1
    right-=1
print(average , len(set(average)))