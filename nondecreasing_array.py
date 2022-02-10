# if 2 dips => false 
# if 0 dip => true 

def nondecreasing(nums):
    idx = None
    for i in range(len(nums)-1):
        if nums[i]> nums[i+1]:
            if idx is not None:
                return False
            idx = i
    # no decreases
    if idx is None:
        return True
    #  if one decrease
    if idx == 0 or idx == len(nums) -2 or nums[idx]<=nums[idx+2] or nums[idx-1]<= nums[idx+1]:

        return True

    return  False
    

