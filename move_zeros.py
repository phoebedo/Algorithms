# LC283e Move all zeros to the back 

def moveZeros(nums):
    cnt = nums.count(0)
    
    while 0 in nums:
        nums.remove(0)
        
    for i in range(cnt):
        nums.append(0)
    return nums


def moveZeros(nums):
    # Idea: have a slow pointer pointing at the beginning and only move with condition.
        # Condition: when iterating nums, if we encounter a nonzero, swap places with the slow and increase slow by 1.
        slow = 0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[i], nums[slow] = nums[slow], nums[i]
                slow+=1


def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        i = 0  # Track Non-zero
     
        for j in range(len(nums)):
            if nums[j] != 0:
               nums[i] = nums[j]
               i += 1 
     
        for i in range(i,j+1):
           nums[i] = 0
                
        return nums