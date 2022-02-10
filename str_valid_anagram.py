# LC242e
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

def isAnagram(s, t):
    sArr, tArr = list(s), list(t)
    sArr.sort()
    tArr.sort()
    
    if len(sArr) != len(tArr):
        return False
    
    for i in range(len(sArr)):
        if sArr[i] == tArr[i]:
            continue
        else:
            return False
    return True


# Solution 2:
# Faster-Hash map. Time O(n). Space O(n) for the map
def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        chars = {}
        for c in s:
            chars[c] = 1+ chars.get(c,0)
        for c in t: 
            if c in chars: 
                chars[c] -=1
        return True if max(chars.values()) == 0 else False