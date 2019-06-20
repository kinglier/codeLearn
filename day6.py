#2019.6.19 lixs
# Palindrome Number

"""
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        palindrome = int(str(x)[::-1])
        if palindrome == x:
            return True
        return False

