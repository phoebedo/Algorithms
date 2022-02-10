# LC647m
# Given a string s, return the number of palindromic substrings in it.
def countSubstrings(s):
    res = 0
    for i in range(len(s)):
        l,r=i,i
        while l>=0 and r <len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1
        
        l,r = i, i+1
        while l>=0 and r <len(s) and s[l] == s[r]:
            res+=1
            l -= 1
            r += 1

    return res