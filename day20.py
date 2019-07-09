#2019.7.9 lixs
#permutations


"""
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""
from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []
        res = []
        self._dfs(nums,[],res)
        return res


    def _dfs(self,nums,path,res):
        if len(nums) == len(path):
            res.append(path[:])
            return
        for i in nums:
            if i not in path:
                path.append(i)
                tmp = path[:]
                self._dfs(nums,path,res)
                path.pop()


class Solution1:
    def permute(self, nums: [int]) -> [[int]]:
        self.res = []
        self.swap(nums, 0)
        return self.res

    def swap(self, nums, j):
        if j == len(nums) - 1: self.res.append(list(nums))
        for i in range(j, len(nums)):
            nums[i], nums[j] = nums[j], nums[i]
            self.swap(nums, j+1)
            nums[i], nums[j] = nums[j], nums[i]


if __name__ == "__main__":
    train = Solution()
    nums = [1,2,3]
    result = train.permute(nums)
    print(result)
