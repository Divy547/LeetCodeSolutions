# Last updated: 11/13/2026, 11:19:17 PM
1class Solution:
2    def singleNonDuplicate(self, nums: List[int]) -> int:
3        l, r = 0, len(nums) - 1
4
5        while l < r:
6            mid = (l + r) // 2
7
8            if mid % 2 == 1:
9                mid -= 1
10
11            if nums[mid] == nums[mid + 1]:
12                l = mid + 2
13            else:
14                r = mid
15
16        return nums[l]