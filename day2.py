#2019.6.14 lixs
#Longest Substring without Repeating Characters

"""
wasted about one hour during this test
The obstacle is I know so little knowledge about the String operation
such as str.find, str[:::], for c in str even str[index]
Finally, I have to search some previous work to learn how to solve this problem
Anyway, We finish it, congratulation!

The highlight of his solution  is he/she use a 'Substring' to record the position of the string
when the dupulicate happen, reset the start position of the 'Substring
"""

class Solution:
    def lengthOfLongestSubstring(self,s:str) -> int:
        substring, length, max_len = "",0,0
        for c in s:
            if c in substring:
                index = substring.find(c)
                substring = substring[(index+1)::]
            substring +=c
            length = len(substring)

            if length > max_len:
                max_len = length
        return max_len


if __name__ == '__main__':
    s = 'abcabc'
    train = Solution()
    max_len = train.lengthOfLongestSubstring(s)
    print(max_len)
