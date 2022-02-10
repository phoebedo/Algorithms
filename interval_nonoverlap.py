# LC435m
# return minimum of intervals to be removed to make the rest intervals non-overlapping

def eraseOverlapIntervals(intervals):
    intervals.sort()
    count=0
    prevEnd = intervals[0][1]
    for start,end in intervals[1:]:
        if start >= prevEnd:
            prevEnd= end
        else:
            count +=1
            prevEnd = min(prevEnd,end) 
    return count
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))

# TIme O(nlogn)
# Space O(1)