# Last updated: 10/30/2026, 2:20:04 PM
1class Solution:
2    def countPairs(self, nums, target):
3        left = 0
4        right = len(nums) - 1
5        count = 0
6        while left < right:
7            if nums[left] + nums[right] <= target:
8                count += right - left
9                left += 1
10            else:
11                right -= 1
12
13        return count
14
15    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
16        
17        nums.sort()
18        return self.countPairs(nums, upper) - self.countPairs(nums, lower - 1)
19