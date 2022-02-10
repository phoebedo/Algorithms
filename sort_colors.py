# given n objects with 3 different colors red(0), white(1), blue(2)
# Input: [1,2,0,0,2,1] -> [0,0,1,1,2,2]
# Note: sort in-place

def sort_colors(n):
    p0=0
    p1=0
    p2=len(n)-1
    while p1<= p2:
        if n[p1]==0:
            n[p0], n[p1] =n[p1], n[p0]
            p1 +=1
            p0 += 1

        if n[p1] == 1:
            p1 += 1
        if n[p1] ==2:
            n[p0],n[p2] = n[p2], n[p0]
            p2 -=1   

