# Last updated: 11/20/2026, 11:10:44 PM
1class Solution:
2    def minPathSum(self, grid: List[List[int]]) -> int:
3        m, n = len(grid), len(grid[0])
4        dp = [0] * n
5        for i in range(m):
6            for j in range(n):
7                if i == 0 and j == 0:
8                    dp[j] = grid[0][0]
9                elif i == 0:
10                    dp[j] = dp[j-1] + grid[i][j]
11                elif j == 0:
12                    dp[j] = dp[j] + grid[i][j]
13                else:
14                    dp[j] = min(dp[j], dp[j-1]) + grid[i][j]
15        return dp[-1]
16