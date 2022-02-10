# note: handle edge cases 
# ditgit*10 +nextdigit


def str_to_int(s:str):
    if not s:
        return None
    
    res = 0
    is_negative = bool(s[0]=="-")

    if is_negative:
        s = s[1:]
        
    for c in s: 
        if not c.isdigit:
            return None
        digit = ord(c) - 48
        res = res*10 + digit

    return -res if is_negative else res


print(str_to_int("-105"))