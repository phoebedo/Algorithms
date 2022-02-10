#LC121e

def stock(nums):
    profit = 0 
    buy= 0
    sell = 1
    while sell< len(nums):
        profit = max(profit, nums[sell]-nums[buy])
        if nums[sell] < nums[buy]:
            buy = sell 
        sell += 1
        
    return profit
        
print(stock([7,6,4]))


    