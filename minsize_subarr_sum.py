# given an array of integers, a positive number s. find minimal length of contiguous subarray which sum >= s.
# Input s=7, array = [2,3,1,2,4,3]
# Output 2 (subarr [4,3])

# def min_subarr_len(nums,s):
#     total = sum(nums)
#     if total< s:
#         return None
#     p1 = 0
#     p2 = len(nums)-1

#     while p1 != p2:
#         if nums[p1] >= s or nums[p2] >= s:
#             return 1
#         if nums[p1] < nums[p2] and (total - nums[p1]) >= s:
#             total = total - nums[p1]
#             p1 += 1
#         elif nums[p1] > nums[p2] and (total - nums[p2]) >=s:
#             total = total - nums[p2]
#             p2 -= 1
#         elif nums[p1] == nums[p2] and (total - nums[p1])>= s:
#             if nums[p1+1] < nums[p2-1]:
#                 p1 += 1
#                 total -= nums[p1]
#             else: 
#                 p2 -= 1
#                 total -= nums[p2]
#         if total <= s:
#             break
        
#     return p2 - p1 +1




# print(min_subarr_len([2,4,1,3,2,3],100))


def min_subarr_len(nums,s):
    res = float("inf")
    sum = 0 
    left = 0 
    right= 0 

    while right<len(nums):
        sum+= nums[right]
        while sum >= s:
            res = min(res, right-left+1)
            sum -= nums[left]
            left += 1
        right += 1
    if res == float('inf'):
        return 0
    return res

            

