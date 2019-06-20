#2019.6.17
#Longest Palindromic Substring

"""
I have not finish this code
even it waste me a lot of time

"""


class Solution:
    def judgeIsDuplicate(self,string):
        for i in range(len(string)-1):
            substring = string[i+1:]
            if string[i] in substring:
                return True
        return False
    def longestPalindrome(self, s: str) -> str:
        lib = {}
        longest = ''
        for i in range(len(s)):
            if s[i] in lib:
                index = lib[s[i]]
                substring = s[index:i+1]
                if not self.judgeIsDuplicate(substring[:-1]):                    
                    if len(substring) > len(longest):
                        longest = substring
                lib[s[i]] = i
            else:
                lib[s[i]] = i
             
        return longest
     
     

strings = ['babad','cbbd','alfja;gj;ag','alafasdkg','abcd']
for string in strings:
    train = Solution()
#    re = train. judgeIsDuplicate(string)
#    print(re)
    result = train.longestPalindrome(string)
    print(result)
