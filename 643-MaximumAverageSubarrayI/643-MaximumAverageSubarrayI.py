# Last updated: 8/9/2025, 2:26:47 AM
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i = 0
        j = k
        winSum = sum(nums[:k])
        maxSum = winSum
        for i in range(k, len(nums)):
            winSum = winSum - nums[i - k] + nums[i]
            maxSum = max(maxSum, winSum)
        return maxSum/k