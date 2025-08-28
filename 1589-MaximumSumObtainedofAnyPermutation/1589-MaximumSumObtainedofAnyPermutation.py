# Last updated: 8/28/2025, 11:51:17 PM
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])
        res = [[0]*m for _ in range(n)]
        for i in range(len(matrix)):
            for j in range(n):
                res[j][i] = matrix[i][j]
        return res  
            