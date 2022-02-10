# very easy. Time O(n) space O(n)
def first_recurring(string:str):
    unique = set()
    for c in string: 
        if c in unique:
            return c
        unique.add(c)
    return None

print(first_recurring("qqwesfdsw"))