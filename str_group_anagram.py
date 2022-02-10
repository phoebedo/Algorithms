# LC49m
# Given an array of strings strs, group the anagrams together. 


from collections import defaultdict
from email.policy import default


def groupAnagrams(strs):
    res = defaultdict(list) 

    for s in strs:
        count = [0]*26
        for c in s:
            count[ord(c)-ord("a")] +=1
        # print(count, tuple(count))
        res[tuple(count)].append(s) 
    
    return res.values()
        
print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

# Time O(n*m) [num_of_str*average_str_len]