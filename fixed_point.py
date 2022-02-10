# Fixed point where value = Index
# given a sorted list of distinct elems. find fixed point if not return None


def binary_search(low,high,nums):
    if low==high:
        return None
    mid= (low+high)//2
    if nums[mid] == mid:
        return mid
    if nums[mid] < mid:
        return binary_search(mid+1,high,nums)
    return binary_search(low,mid,nums)
def find_fixed_point(nums):
    return binary_search(0,len(nums),nums)

print(find_fixed_point([-1,0,2,4,8,11,13]))