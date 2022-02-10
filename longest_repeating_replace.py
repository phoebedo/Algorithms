#LC424m 
# You are given a string s and an integer k.
# Return the length of the longest substring containing the same letter you can get after performing the above operations.

def characterReplacement(s,k):
    count = {}
    res = 0
    l = 0 
    for r in range(len(s)):
        count[s[r]] = 1+ count.get(s[r],0)
        # shift left pointer when window invalid
        while (r-l+1) - max(count.values()) >k:
            count[s[l]] -=1
            l+=1

        res = max(res,r-l+1)
    return res

