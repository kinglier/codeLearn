#2019.7.31 lixs
#Sqrt(x)

"""
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since
             the decimal part is truncated, 2 is returned.

"""

class Solution:
    def mySqrt(self, x: int) -> int:

        #using binary search idea
        if x==1:
            return 1

        right=x
        left=0
        res = (right+left)/2

        while (abs(res*res - x)>0.05):
            if res**2 > x:
                right=res
            elif res**2 < x:
                left=res

            res=(right+left)/2.0

        return int(res)
