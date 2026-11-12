# Last updated: 11/12/2026, 10:09:04 PM
1
2class Solution:
3    def findPeakElement(self, nums: List[int]) -> int:
4        left, right = 0, len(nums) - 1
5
6        while left < right:
7            mid = (left + right) // 2
8
9            if nums[mid] > nums[mid + 1]:
10                right = mid
11            else:
12                left = mid + 1
13
14        return left
15