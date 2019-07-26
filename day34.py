#2019.7.26 lixs
# Minimum Path Sum

"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
"""
from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        res =0
        path = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        if len(grid) == 0: return res
        path[0][0] = matrix[0][0]
        # initialize the first row
        i = 1
        while i < len(matrix[0]):
            path[0][i] = path[0][i-1] + matrix[0][i]
            i += 1
         
        # inintialize the first column
        j = 1
        while j < len(matrix):
            path[j][0] = path[j-1][0] + matrix[j][0]
            j += 1

        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                path[i][j] = min(path[i-1][j], path[i][j-1]) + matrix[i][j]

        print(path)
        return path[-1][-1]


if __name__ == "__main__":
    train = Solution()
    matrix = [
             [1,3,1],
             [1,5,1],
             [4,2,1]
             ] 
    res = train.minPathSum(matrix)
    print(res)
