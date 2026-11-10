# Last updated: 11/11/2026, 12:07:58 AM
1
2class Solution:
3    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
4        m, n = len(matrix), len(matrix[0])
5
6        left, right = 0, m * n - 1
7
8        while left <= right:
9            mid = (left + right) // 2
10
11            row = mid // n
12            col = mid % n
13
14            if matrix[row][col] == target:
15                return True
16            elif matrix[row][col] < target:
17                left = mid + 1
18            else:
19                right = mid - 1
20
21        return False
22