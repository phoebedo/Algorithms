# LC91m - FB
# Recursive
def decode_ways(s):
    dp = {len(s):1}

    def dfs(i):
        if i in dp:
            print("dp",i, ": ", dp[i])
            return dp[i]
        if s[i] == "0":
            return 0
        
        res = dfs(i+1)
        if i+1 < len(s) and((s[i]=="1") or (s[i]=="2" and s[i+1] in '123456')):
            res += dfs(i+2)
        dp[i]= res
        return res
    return dfs(0)
# dynamic programming - bottom up 
def decode_ways_dp(s):
    dp = {len(s):1}

    for i in range(len(s)-1,-1,-1):
        if s[i] == "0":
            dp[i] = 0
        else:
            dp[i] = dp[i+1]

        if (i+1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i+1] in "123456"))):
            dp[i] += dp[i+2]
    return dp[0]
s = '1210'
print(decode_ways_dp(s))