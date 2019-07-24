#2019.7.24 lixs
# unique path

"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right

"""
from typing import List
import math

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cur = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                print(i,j)
                cur[j] += cur[j-1]
                print(cur)
        return cur[-1]
    def uniquePaths1(self, m: int, n: int) -> int:
        matrix = [[0 for _ in range(n+1)] for _ in range(m+1)]
        matrix[0][1] = 1
        print(matrix)
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]
                print(matrix)
        return matrix[-1][-1]
    def uniquePaths2(self, m: int, n: int) -> int:
        return int(math.factorial(m+n-2)/math.factorial(m-1)/math.factorial(n-1))



if __name__ == "__main__":
    m = 3
    n = 2
    train = Solution()
    result = train.uniquePaths2(m,n)
    print(result)


