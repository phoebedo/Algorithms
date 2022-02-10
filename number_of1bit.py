# Given a number. COunt how many 1 in its binary representation
# Bitwise operators: << >> & | ~ ^ 

def one_bits(num):
    count =0 
    while num > 0:
        if num &1 == 1:
            count += 1
        num >>= 1
    return count
print(one_bits(23))


