#2019.6.27 lixs
# Letter Combinations of a Phone Number

#"""
#Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
#
#A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
#
#Input: "23"
#Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
#
#"""

from typing import List

class Solution:

    def getLatter(self, digits):
        maps = {'2':"abc", '3':"def", '4':"ghi", '5':"jkl", '6':"mno", '7':"pqrs", '8':"tuv", '9':"wxyz"}
        res = []
        for i in digits:
            print(i)
            print(type(i))
            print(maps[str(i)])
            if not res:
                res = res + [x for x in maps[str(i)]]
            else:
                res = [x+y for x in res for y in maps[str(i)]]
        return res



if __name__ == "__main__":
    train = Solution()
    digits = [2,3]
    result = train.getLatter(digits)
    print(result)
