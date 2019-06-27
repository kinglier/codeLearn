


class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        if len(matrix)%2 == 0:
            for i in range(int(len(matrix)/2)):
                for j in range(int(len(matrix)/2)):
                    print(i,j)
                    matrix =self.singleTurn(matrix,i,j)
        else:
            for i in range(len(matrix)//2):
                for j in range(len(matrix)//2+1):
                    matrix =self.singleTurn(matrix,i,j)
        return matrix
    def singleTurn(self,matrix,raw,colunm):
        N = len(matrix) - 1
        positions = self.threeSymmetryPoints(raw,colunm,N)
        tmp = matrix[positions[0][0]][positions[0][1]]
        matrix[positions[0][0]][positions[0][1]] = matrix[positions[3][0]][positions[3][1]]
        matrix[positions[3][0]][positions[3][1]] = matrix[positions[2][0]][positions[2][1]]
        matrix[positions[2][0]][positions[2][1]] = matrix[positions[1][0]][positions[1][1]]
        matrix[positions[1][0]][positions[1][1]] = tmp
        return matrix 

    def threeSymmetryPoints(self,raw,colunm,N):
        position0 = [raw,colunm]
        position1 = [colunm,N-raw]
        position2 = [N-raw,N-colunm]
        position3 = [N-colunm,raw]
        return ([position0,position1,position2,position3])


if __name__ == "__main__":
    train = Solution()
    matrix = [
              [1,2,3],
              [4,5,6],
              [7,8,9]
              ]
    matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    result = train.rotate(matrix)
    print(result)
