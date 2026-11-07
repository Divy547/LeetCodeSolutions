# Last updated: 11/7/2026, 10:59:46 PM
1class Solution:
2    def waysToSplitArray(self, nums: List[int]) -> int:
3        total = sum(nums)
4        left_sum = 0
5        count = 0
6
7        for i in range(len(nums) - 1):
8            left_sum += nums[i]
9            right_sum = total - left_sum
10
11            if left_sum >= right_sum:
12                count += 1
13
14        return count