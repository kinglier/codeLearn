#2019.7.25 lixs
# unique pathII

"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Note: m and n will be at most 100.

Example 1:

Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2

"""
from typing import List
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        dp = [[0]*col for i in range(row)]

        if obstacleGrid[0][0] ==1 or obstacleGrid[-1][-1] ==1:
            return 0


        i = 0
        while i < col and obstacleGrid[0][i] == 0:
            dp[0][i] = 1
            i+=1
        for x in range(i, col):
            dp[0][x] = 0

        j = 0
        while j < row and obstacleGrid[j][0] == 0:
            dp[j][0] = 1
            j+=1
        for y in range(j, row ):
            dp[y][0] = 0


        for i in range(1, row):
            for j in range(1, col):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] =0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[-1][-1]

if __name__ == "__main__":
    train = Solution()
    matrix = [
             [0,0,0],
             [0,1,0],
             [0,0,0]
             ]
    result = train.uniquePathsWithObstacles(matrix)
    print(result)

