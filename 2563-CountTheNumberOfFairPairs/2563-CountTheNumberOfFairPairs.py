# Last updated: 11/4/2026, 9:51:40 PM
class Solution:
    def countPairs(self, nums, target):
        left = 0
        right = len(nums) - 1
        count = 0
        while left < right:
            if nums[left] + nums[right] <= target:
                count += right - left
                left += 1
            else:
                right -= 1

        return count

    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        
        nums.sort()
        return self.countPairs(nums, upper) - self.countPairs(nums, lower - 1)
