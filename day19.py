#2019.7.8 lixs
#conbination sum

"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
"""

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if len(candidates) == 0:
            return []
        res = []
        candidates.sort()
        self._dfs(candidates,0,target,[],res)

        return res


    def _dfs(self,candidates,start,residue,path,res):
        if residue == 0:
            if path[:] not in res:
                res.append(path[:])
            return
        for index in range(start,len(candidates)):
            if residue - candidates[index] < 0:
                break
            path.append(candidates[index])
            self._dfs(candidates,index+1,residue - candidates[index],path,res)
            path.pop()
