#LC238e 
# I: [1,2,3,4]
#O: [1,1,1,1]
# [1,1,2,6] (res[i] = res[i-1]* nums[i-1])
# [24,12,8,6] right *= nums[i+1] 
            # res[i] *= right

def prod_except_self(nums):
    res = [1] * len(nums)

    for i in range(1,len(nums)):
       res[i] = res[i-1]* nums[i-1]
    right =1
    for i in range(len(nums)-2,-1,-1):
        right *= nums[i+1] 
        res[i] *= right
    return res

print(prod_except_self([1,2,3,4]))