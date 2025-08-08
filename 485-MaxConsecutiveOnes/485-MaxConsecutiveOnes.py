# Last updated: 8/9/2025, 2:26:49 AM
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i = 0
        maxLen = 0
        for j in range(0, len(nums)):
            if nums[j] != 1:
                i = j + 1
            
            maxLen = max(maxLen, j - i + 1)
        return (maxLen)