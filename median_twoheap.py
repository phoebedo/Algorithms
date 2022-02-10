# Compute the median for each new element
#Method 1: Sorted array . Time complexity O(N**2) space O(N)
#Method 2: Optimal. 2 heap technique

import heapq
#Note: heapq is using min heap implementation. If want to use max heap => make it negative number

def add(num, min_heap, max_heap):
    if len(min_heap) + len(max_heap) <=1:
        heapq.heappush(max_heap, -num)
        return
    median = get_median(min_heap,min_heap)
    if num> median:
        heapq.heappush(min_heap, num)
    else:
        heapq.heappush(max_heap, -num)
    

def rebalance(min_heap, max_heap):
    if len(min_heap) > len(max_heap) +1:
        root = heapq.heappop(min_heap)
        heapq.heappush(max_heap, -root)
    elif len(max_heap) > len(min_heap)+1:
        root = -heapq.heappop(max_heap)
        heapq.heappush(min_heap, root)

def get_median(min_heap, max_heap):
    if len(min_heap)>len(max_heap):
        return min_heap[0]
    elif len(min_heap)<len(max_heap):
        return -max_heap[0]
    else:
        return (min_heap[0]-max_heap[0])/2.0


def running_median(nums):
    min_heap = []
    max_heap = [] 

    for num in nums:
        add(num, min_heap, max_heap)
        rebalance(min_heap, max_heap)
        print(get_median(min_heap, max_heap))

 
running_median([2,1,4,7,2,0,5])