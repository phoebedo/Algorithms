import collections
def find_anagram(s,t):
    res =[]
    ch_map = collections.defaultdict(int)

    for ch in t:
        ch_map +=1

    for i in range(len(s)):
        ch = s[i]

        if i >= len(t):
            old_ch =s[i -len(t)]
            ch_map[old_ch]+=1
            if ch_map[old_ch] ==0:
                del ch_map[ch]

        ch_map[ch] -=1
        if ch_map[ch] ==0:
            del ch_map[ch]
        if i+1 >= len(t) and len(ch_map)==0:
            res.append(i -len(t)+1)
    return res