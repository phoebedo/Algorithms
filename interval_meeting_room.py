# LC252e premium
# Lintcode
#each: [starttime, endtime]
#  [[s1,e1],[s2,e2],....]
# bool(a person can attend all meetings?)
# note e1 = s2 => not conflict
def meeting_room(intervals):
    intervals.sort()
    prevEnd = intervals[0][1]
    for start,end in intervals[1:]:
        if start<prevEnd:
            return False
        else:
            prevEnd = end
    return True

print(meeting_room([[0,10],[18,30],[15,20]]))

# Time O(n)
# Space O(1)

# What if interval is an object. (interval.start, interval.end)?

