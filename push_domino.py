# LC838m
# Input ".L.R...LR..L.."
# Output "LL.RR.LLRRLL.."
def push_dominoes(dominoes:str):
    N = len(dominoes)
    force = [0]*N
    f=0
    for i in range(N):
        if dominoes[i] == "R":
            f = N
        elif dominoes[i]=="L":
            f = 0
        else:
            f = max(f-1,0)
        force[i] += f
    
    for i in range(N-1,-1,-1):
        if dominoes[i] == "L":
            f = N 
        elif dominoes[i] == "R":
            f = 0 
        else:
            f = max(f-1,0)
        force[i] -= f
    
    res = ''
    for i in range(N):
        if force[i]<0:
            res += "L"
        if force[i]>0:
            res +="R"
        if force[i]==0:
            res += "."

    return res

print(push_dominoes(".L.R...LR..L.."))
print(push_dominoes(
"RR.L"))