# LC253m Premium 
# Lintcode919

"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def minMeetingRooms(self, intervals):
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])
        res,count=0,0
        s,e=0,0
        while s<len(intervals):
            if start[s]<end[e]:
                count +=1 
                s +=1
            else:
                e +=1
                count +=1
            res = max(res,count)
        return res
        # Write your code here
