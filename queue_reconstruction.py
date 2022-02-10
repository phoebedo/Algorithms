# Queue reconstruction by height LC406m
# List of people standing in a queue. \
# (h,k): h is height. k: num of ppl >= heigh in front
# Reconstruct the queue that is represented by the input array. 


def reconstructQueue(people):
    people.sort(key=lambda x:(-x[0],x[1]))
    res = []

    for p in people:
        res.insert(p[1],p)
    return res
    