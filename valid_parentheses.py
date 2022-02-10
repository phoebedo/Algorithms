# LC20e 
# Valid perantheses
def valid_peran(s:str):
    pairs={
        "}" :"{",
        ")":"(",
        "]" :"["}
        
    if len(s) ==0:
        return True

    stack = [s[0]]
    for c in s[1:]:
        if c in pairs and len(stack)>0 and pairs[c] == stack[0]:
            stack.pop(0)
        else:
            stack.insert(0,c)

    return True if len(stack) == 0 else False