# Given a list of sorted numbers, return the list of square in sorted order 
def sorted_square(nums):
    res = []
    left = 0
    right = len(nums) -1 
    while left <= right:
        print(left,right)
        if nums[left]**2 <= nums[right]**2:
            res.insert(0,nums[right]**2)
            right -=1
        else:
            res.insert(0,nums[left]**2)
            left +=1
    return res

print(sorted_square([-5,-1,0,1,4,5]))
