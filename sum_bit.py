import math
def getSum(self, a: int, b: int) -> int:
        #raises 2 to the power a
        fact1=math.pow(2,a)
        #raises 2 to the power b
        fact2=math.pow(2,b)
        #by multiplying the 2 factors, the powers gets added
        #ie, 2^(a+b)
        prod=fact1*fact2
        """
         here we use the Log of Exponent Rule 
            -> log2(2^(a+b)) = a+b
         """
        ans=math.log(prod,2)
        return int(ans)


# Bit manipulation 
class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xffffffff
        while b:
            carry = a&b
            a = (a ^ b) & MASK
            b = (carry << 1) & MASK
            
        if (a>>31) & 1:
            return ~(a^MASK)
        return a
# The solution in Python is different than other languages because in Python it considers the unlimited length of integers whereas in other languages integers has fixed length of 32-bit.
# If we perform the normal bit manipulation solution in python then the loop runs for infinite times as integers are not fixed to 32-bit. To avoid this in python we use a MASK 0xffffffff to keep the integer in 32-bits.
# At last we have conditions to return the value because especially for negative integers we have to first calculate the two's complement of the returning number. But only ~a will flip infinite bits of a and hence we have limit it in 32-bit using MASK. Thus we xor a with mask and finally return ~(a^MASK).