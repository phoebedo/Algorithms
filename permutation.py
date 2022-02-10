# LC46m
def permute(nums): 

    res = []
    def permuteHelper(start):
        # base case: only have one num. No more option
        if start ==len(nums)-1:
            res.append(nums[:])
        
        for i in range(start,len(nums)):
            nums[start], nums[i] = nums[i], nums[start]
            permuteHelper(start+1)
            nums[start], nums[i] = nums[i], nums[start]    
    permuteHelper(0)   
    return  res