# Last updated: 8/30/2025, 11:51:45 PM
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        diagSum = 0
        for i in range(0, len(mat)):
            for j in range(0, len(mat)):
                if i == j or i + j == len(mat) - 1:
                    diagSum += mat[i][j]
        return diagSum