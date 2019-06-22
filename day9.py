#2019.6.22
#Valid Parentheses

"""
The stack data structure is very useful
"""

class Solution:
    def isValid(self,s):
        lib = {'(':')','[':']','{':'}'}
        stack = []
        for i in range(len(s)):

            if s[i] in lib:
                stack.append(s[i])
            elif len(stack) == 0 or lib[stack.pop()] != s[i]:
                return False
        if len(stack) != 0: return False
        else: return True

if __name__ == '__main__':
    string = '()'
    train = Solution()
    print(train.isValid(string))

