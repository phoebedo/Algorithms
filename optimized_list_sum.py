# Sum providing start - end index

# Naive approach
# class ListFastSum:
#     def __init__(self,nums:list) -> None:
#         self.nums = nums

#     def sum(self,start_idx, end_idx):
#         total = 0
#         for i in range(start_idx, end_idx):
#             total += self.nums[i]
#         return total

# l = ListFastSum([1,2,3,4,5,6,7])

# print(l.sum(2,5))


# Pre-computing - OPTIMIZED. Time O(n). Space O(n)
# [1,2,3,4,5,6,7]
# [1,3,6,10,15,21,28] Precompute up-to sum 
# sum = sum_up_to[end-1]- sum_up_to[start-1]

class ListFastSum:
    def __init__(self,nums:list) -> None:
        self.nums = nums
        self.sum_up_to = []

        curr_sum = 0
        for num in nums:
            curr_sum += num
            self.sum_up_to.append(curr_sum)
        self.sum_up_to.append(0)

    def sum(self,start_idx, end_idx):
        return self.sum_up_to[end_idx-1] - self.sum_up_to[start_idx-1]

l = ListFastSum([1,2,3,4,5,6,7])

print(l.sum(2,5))
