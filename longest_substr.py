# LC3m
# Longest substring without repeating chars

# Brute force approach. Loop(i,j) => Double loop O(n**2). 
# Each time, have to look at the substring 
# ? if there's repeating characters =>
# Total time complexity O(N**4)

# !!!  can skip the current loop whenever it begins to have repeating characters 
# SLIDING WINDOW method. Time O(N)+(ON) => O(N)
import re


def lengthOfLongestSubstring(s):
    charSet = set()
    l = 0 
    res = 0 
    for r in range(len(s)):
        while s[r] in charSet:
            charSet.remove[s[l]]
            l+=1
        charSet.add(s[r])
        res = max(res, r-l +1)
    return res
    
# Even better: still O(N) but optimal space complexity...
def lengthOfLongestSubstring(s:str)->int:
    letters = {} #char:index (index last seen)
    tail= -1
    head = 0
    result = 0

    while head< len(s):
        if s[head] in letters: 
            tail = max(tail,letters[s[head]]) #skip all if see repeating char
        letters[s[head]] = head #if not, push letter to dict
        result = max(result, head-tail) #length of current = head-tail
        head +=1
    
    return result

print(lengthOfLongestSubstring("pwwkew"))
 