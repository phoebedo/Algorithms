#LC198m
def house_robber(nums):
    dp = [0]*(len(nums)+1)
    # Rob 0 house
    dp[0]=0
    # Rob first house 
    dp[1]= nums[0]
    
    for i in range(2,len(dp)):
        dp[i] = max(dp[i-1], dp[i-2]+ nums[i-1])

    return dp[-1]

print(house_robber([2,1,1,2]))