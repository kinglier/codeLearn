#2019.7.30 lixs
#add binary

"""
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
         print(bin(int(a,2)+int(b,2)))
         return str(bin(int(a,2)+int(b,2)))[2:]

if __name__ == "__main__" :
    train = Solution()
    a = "11"
    b = "1"
    res = train.addBinary(a,b)
    print(res)
