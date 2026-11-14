# Last updated: 11/14/2026, 11:24:36 PM
1
2class Solution:
3    def minEatingSpeed(self, piles: List[int], h: int) -> int:
4        left, right = 1, max(piles)
5
6        while left < right:
7            mid = (left + right) // 2
8
9            hours = sum((p + mid - 1) // mid for p in piles)
10
11            if hours <= h:
12                right = mid
13            else:
14                left = mid + 1
15
16        return left
17