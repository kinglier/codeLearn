#2019.6.26 lixs
#divide two interger

"""
  Though this exercise I learn some useful skill
  abs()
  1 << 2 = 1*2**2
  return min(max(-2**31, result), 2**31-1)
"""

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sigh1 = sigh2 = 1
        result = 0
        if dividend < 0:
            dividend = -dividend
            sigh1 = -1
        if divisor < 0:
            divisor = -divisor
            sigh2 = -1
        while dividend >= divisor:
            dividend = dividend - divisor
            result += 1
        if sigh1 == -1 and sigh2 ==1:
            result = 0 - result
        if sigh1 == 1 and sigh2 == -1:
            result = 0 - result
        if result < (-2**31):
            return (-2**31)
        elif result > 2**31:
            return 2**31
        else:
            return result
    def divide1(sefl,dividend,divisor):
        a,b,r,t = abs(dividend), abs(divisor),0,1
        while a>=b or t>1:
            if a>=b or t>1:
                if a>=b: r+=t; a-=b; t+=t; b+=b
                else:t>>=1; b>>=1
        return min((-r, r)[dividend ^ divisor >= 0], (1 << 31) - 1)
if __name__ == "__main__":
    train = Solution()
    devidend = 1
    devidor = 1
    result = train.divide1(devidend,devidor)
    print(result)
