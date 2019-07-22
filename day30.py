#2019.7.22 lixs
#permutation

"""
The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note:

Given n will be between 1 and 9 inclusive.
Given k will be between 1 and n! inclusive.
Example 1:

Input: n = 3, k = 3
Output: "213"
Example 2:

Input: n = 4, k = 9
Output: "2314"
"""

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [i for i in range(1,n+1)]
        res = []
        self._dfs(nums,[],res)
        res.sort()
    
        return "".join(str(res[k-1][i]) for i in range(n))


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

    def getPermutation1(self, n: int, k: int) -> str:
        return "".join (str(z) for z in list(itertools.permutations(range(1,n+1),n))[k-1])
if __name__ == "__main__":
    train = Solution()
    n = 3 
    k = 3
    result = train.getPermutation(n,k)
    print(result)
