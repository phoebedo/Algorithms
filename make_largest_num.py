# given a list in integers make the largest number buy combining them

# Input [17,7,2,45,72] => 77245217

from functools import cmp_to_key

def largest_num(nums):
    def compare(a,b):
        return 1 if str(a)+str(b)<str(b)+str(a) else -1
        
    str_num=[str(n) for n in sorted(nums, key=cmp_to_key(compare))]
    return ''.join(str_num)

print(largest_num([17,7,2,45,72]))