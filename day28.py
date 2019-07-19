#2019.7.19 lixs
#str最大长度


"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:

Input: "Hello World"
Output: 5
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        mid = s.strip().split(" ")
        print(mid)
        if(mid[-1] == ""):
            return 0
        elif(mid[-1] != ""):
            print(mid[-1])
            return len(mid[-1])

if __name__ == "__main__":
    train = Solution()
    s = "I'm The World"
    print(train.lengthOfLastWord(s))
    
