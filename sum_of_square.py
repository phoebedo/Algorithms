# given number n. return least number of squares needed to sum up to the number

def sum_square(n):
    squares = []
    i=1
    while i*i<=n:
        squares.append(i**2)
        i+=1
    
    min_sums = [n] *(n+1)
    min_sums[0]=0
    for idx in range(len(min_sums)):
        for s in squares:
            if idx+s<len(min_sums):
                min_sums[idx+s] = min(min_sums[idx+s],min_sums[idx]+1)
    return min_sums[-1]

    
print(sum_square(13))