# Last updated: 8/9/2025, 2:27:23 AM
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)

        maxCurrent = maxGlobal = nums[0]
        for i in range(1, n):
            maxCurrent = max(nums[i], nums[i] + maxCurrent)
            maxGlobal = max(maxGlobal, maxCurrent)
        return maxGlobal