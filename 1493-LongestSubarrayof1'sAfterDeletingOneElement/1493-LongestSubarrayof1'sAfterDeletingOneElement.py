# Last updated: 8/24/2025, 1:38:13 PM
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        i = 0
        maxLen = 0
        zeroCount = 0
        for j in range(0, len(nums)):
            if nums[j] == 0:
                zeroCount += 1
            if zeroCount > 1:
                if nums[i] == 0:
                    zeroCount -= 1
                i +=1
            
            maxLen = max(maxLen, j - i)
        return (maxLen)