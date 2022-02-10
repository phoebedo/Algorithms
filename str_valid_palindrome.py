# LC125e
# converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, 
# it reads the same forward and backward.

def isPalindrome(s:str):
    # s = ''.join(c.lower() for c in s if c.isalnum())
    # # recursively. !!!callstack when input is large
    # if len(s) <= 1:
    #     return True
    # else:
    #     if s[0] != s[len(s)-1]:
    #         return False
    #     return isPalindrome(s[1:len(s)-1])
    # iteratively 
    if len(s) <= 1:
        return True
    
    l,r = 0, len(s)-1
    while l <r:
        if s[l] != s[r]:
            return False
        l +=1 
        r -=1
    return True


print(isPalindrome("aa"))