import collections
import heapq
def top_k(nums,k):
    count = collections.defaultdict(int)
    for n in nums:
        count[n] +=1
    
    heap = []
    for key,val in  count.items():
        heapq.heappush(heap, (val,key))
        if len(heap) > k :
            heapq.heappop(heap)
    res = []
    while len(heap) >0:
        res.append(heapq.heappop(heap)[1])

    return res 

print(top_k([1,1,1,2,2,3,4],2))

# Note:: 
# For example, your object is something like this in tuple's format (key, value_1, value_2)

# When you put the objects (i.e. tuples) into heap, it will take the first attribute in the object (in this case is key) to compare. If a tie happens, the heap will use the next attribute (i.e. value_1) and so on.