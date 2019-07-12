#2019.7.12 lixs
# 排列组合题

"""
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

"""
from typing import List
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0: return []
        nums.sort()
        res = []
        used = [False] * len(nums)
        self._dfs(nums,[],used,res)
        return res
    def _dfs(self,nums,path,used,res):
        if len(path) == len(nums):
            res.append(path[:])
            return
        for i in range(len(nums)):
            if not used[i]:
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue
                used[i] = True
                path.append(nums[i])
                self._dfs(nums,path,used,res)
                used[i] = False
                path.pop()

if __name__ == "__main__":
    train = Solution()
    nums = [1,1,2]
    result = train.permuteUnique(nums)
    print(result)

