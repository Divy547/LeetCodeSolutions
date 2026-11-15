# Last updated: 11/15/2026, 2:55:13 PM
1
2class Solution:
3    def shipWithinDays(self, weights: List[int], days: int) -> int:
4        left, right = max(weights), sum(weights)
5
6        while left < right:
7            mid = (left + right) // 2
8
9            required_days = 1
10            current_load = 0
11
12            for w in weights:
13                if current_load + w > mid:
14                    required_days += 1
15                    current_load = 0
16
17                current_load += w
18
19            if required_days <= days:
20                right = mid
21            else:
22                left = mid + 1
23
24        return left
25