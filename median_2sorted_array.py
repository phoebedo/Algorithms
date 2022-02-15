#LC4h: find median of two sort array 

# Straight forward: merge 2 sorted arr => find median. Time complx: O(m+n)

# Optimal: Find median without merging. 
# 2 arrays A,B. len(A)<len(B)
# BS on whichever sorter, find pos/ A_leftpartion<B_rightpartition && B_leftpartition <A_rightpartition
# If len(A+B) odd: return max(Aleft, Bleft). 
# If even return  (max(Aleft,Bleft)+min(Aright,Bright))/2
# Time complx O(log(n)) n<m. No extra memory needed

def findMedianSortedArrays(nums1,nums2):
    A,B=nums1, nums2
    total = len(nums1) + len(nums2)
    half = total//2
    
    
    if len(B) <len(A):
        A, B = B, A
        
    l, r = 0,len(A)-1
    
    while True:
        i = (l+r) //2
        j = half - i -2
        
        Aleft = A[i] if i>= 0 else float("-infinity")
        Aright = A[i+1] if (i+1)<len(A) else float("infinity")
        Bleft = B[j] if j>= 0  else float("-infinity")
        Bright = B[j+1] if (j+1) < len(B) else float("infinity")
        
        if Aleft <= Bright and Bleft<= Aright:
            
            if total%2:
                return min(Aright,Bright)
            
            else:
            
                return float(max(Aleft,Bleft) + min(Aright, Bright))/2
            
        
        elif Aleft>Bright:
            r = i-1
        else: 
            l = i+1



print(findMedianSortedArrays([1,2],[3,4]))
