#2019.7.6 lixs
#Combination Sum

"""
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""

class Solution:
    def combinationSum(self,candidates,target):
        if len(candidates) == 0:
            return []
        res = []
        candidates.sort()
        self._dfs(candidates,0,target,[],res)
        
        return res


    def _dfs(self,candidates,start,residue,path,res):
        if residue == 0:
            res.append(path[:])
            return
        for index in range(start,len(candidates)):
            if residue - candidates[index] < 0:
                break
            path.append(candidates[index])
            self._dfs(candidates,index,residue - candidates[index],path,res)
            path.pop()


if __name__ == "__main__":
    train = Solution()
    candidates =  [2,3,5]
    target = 8
    res = train.combinationSum(candidates,target)
    print(res)
