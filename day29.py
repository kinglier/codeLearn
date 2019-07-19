#2019.7.19 lixs
#螺旋矩阵

"""
"""
from typing import List
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        def spiral_coords(r1, c1, r2, c2):
            for c in range(c1,c2+1):
                yield r1, c
            for r in range(r1+1,r2+1):
                yield r,c2
            if r1 < r2 and c1 < c2:
                for c in range(c2-1,c1,-1):
                    yield r2,c
                for r in range(r2,r1,-1):
                    yield r,c1
        res = [[None for _ in range(n)] for _ in range(n)]
        r1,r2 = 0,len(res)-1
        c1,c2 = 0,len(res[0]) -1
        i = 1
        while r1<=r2 and c1 <= c2:
             for r,c in spiral_coords(r1, c1, r2, c2):
                 res[r][c] = i
                 i +=1
             r1 +=1
             r2 -=1
             c1 +=1
             c2 -=1
        return res

if __name__ == "__main__":
    n = 3
    train = Solution()
    res = train.generateMatrix(3)
    print(res)
