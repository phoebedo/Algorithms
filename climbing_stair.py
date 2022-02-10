# Leetcode 70 EZ

# n steps to the top. Each time you can climb 1/2 steps. How many ways to make it to the top 
# Given: n is a positive int

# Recursive: SLOW  O(2**n)
def climb_stair(n):
    if n == 1:
        return 1
    if n== 2: 
        return 2
    return climb_stair(n-1) + climb_stair(n-2)

#Iterative 
def itr_climb_stair(n):
    if n == 1:
        return 1
    if n== 2: 
        return 2
    ways = 0
    first = 1
    second = 2
    for i in range(3,n+1):
        ways = first+second
        first = second
        second = ways
    return ways
    

print(climb_stair(6))
print(itr_climb_stair(6))
