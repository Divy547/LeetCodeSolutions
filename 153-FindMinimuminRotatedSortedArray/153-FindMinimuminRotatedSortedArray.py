# Last updated: 11/11/2026, 11:34:52 PM
1class Solution:
2    def findMin(self, nums: List[int]) -> int:
3        left, right = 0, len(nums) - 1
4
5        while left < right:
6            mid = (left + right) // 2
7
8            if nums[mid] > nums[right]:
9                left = mid + 1
10            else:
11                right = mid
12
13        return nums[left]