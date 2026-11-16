# Last updated: 11/16/2026, 10:25:31 PM
1class Solution:
2    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
3        n = len(bloomDay)
4
5        if m * k > n:
6            return -1
7
8        low = min(bloomDay)
9        high = max(bloomDay)
10
11        def canMake(day):
12            bouquets = 0
13            flowers = 0
14
15            for bloom in bloomDay:
16                if bloom <= day:
17                    flowers += 1
18
19                    if flowers == k:
20                        bouquets += 1
21                        flowers = 0
22                else:
23                    flowers = 0
24
25            return bouquets >= m
26
27        while low < high:
28            mid = (low + high) // 2
29
30            if canMake(mid):
31                high = mid
32            else:
33                low = mid + 1
34
35        return low