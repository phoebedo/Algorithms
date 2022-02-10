# LC56m. 
# given a collection of intervals/ merge all overlaping intervals. 
#  

def merge(intervals):
    intervals.sort(key= lambda inter:inter[0])
    res = []
    for interval in intervals:
        if not res or res[-1][1]<interval[0]:
            res.append(interval)
        else:
            res[-1][1] = max(res[-1][1], interval[1])
    return res
    
