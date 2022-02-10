def coin_change(coins,amount):
    dp = [amount+1]* (amount+1)
    dp[0]=0
    for a in range(1,amount+1):
        for c in coins:
            if a-c >= 0:
                dp[a] = min(dp[a],1+dp[a-c])
            

    return dp[amount+1] if dp[amount+1] != amount+1 else -1

# Time O(coins*amount)
# Space O(amount)