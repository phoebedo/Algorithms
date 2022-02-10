# LC57m
def insert(intervals,newInterval):
    res = []

    for i in range(len(intervals)):
        if newInterval[1]<intervals[i][0]:
            res.append(newInterval)
            return res+ intervals[i:]
        elif newInterval[0]>intervals[i][1]:
            res.append(intervals[i])
        else:
            newInterval =[min(newInterval[0],intervals[i][0]), max(newInterval[1], intervals[i][1])]
    
    res.append(newInterval)
    return res
    

test_intervals = [[1,5]]
test_newInterval = [0,7]
print(insert(test_intervals, test_newInterval))

# Time O(n)
# Space O(n)