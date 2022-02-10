# LC53e
# contiguous sub-array. max sum 

def max_subarr(nums):
    if len(nums) ==0 :
        return 0
    res = nums[0]
    curr_sum = 0

    for n in nums:
        if curr_sum +n <0:
            curr_sum=0
            res= max(n,res) 
        else:
            curr_sum +=n
            res = max(curr_sum,res)
    
    return res




print(max_subarr([-2,-3,-1,-5]))
