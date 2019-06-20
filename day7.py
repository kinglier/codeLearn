# 2019.6.20 lixs
# Longest Common Prefix

"""
The use of the TRY and EXCEPT is very wise
Else I should search the mini long string

It has been one week since I begin to practice in the leedcode
It's very useful since I can get a lot of fundimental knowledge about python
and learn some interesting ways to solve problems

It's still very hard for me to shoulder the work in this company
I'm stress every day but I believe I can do it no matter how difficult it is,
I should conquer it, It's my faith of life.

"""


class Solution:
    def longestCommonPrefix(self,strs):
        if strs == []: return ''
        prefix = ''
        i = 0

        while True:
            try:
                for j in range(0,len(strs)):
                    if strs[j][i] != strs[0][i]: return prefix

                prefix = prefix + strs[0][i]
            except IndexError: return prefix

            i +=1
        return prefix





