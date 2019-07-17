#2019.7.17 lixs
#jump game

"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index
"""
from typing import List

class Solution:
    def jumpGame(self,nums):
        if len(nums) <=1: return True
        for i in range(len(nums)-2,-1,-1):
            if nums[i] == 0:
                res = False
                for j in range(i):
                    if i - j < nums[j]:
                        res = True
                        break
            if not res: return res
        return True
    def jumpGame2(nums):
        max_ix = 0
        for i,item in enumerate(nums):
            if i <= max_ix:
                if i + item > max_ix:
                    max_ix = i + item
            else:
                break
        return max_ix >= len(nums) -1

if __name__ == "__main__":
    train = Solution()
    nums = [3,2,1,0,4]
    result = train.jumpGame(nums)
    print(result)
