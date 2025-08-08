# Last updated: 8/9/2025, 2:26:40 AM
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i = 0
        maxLen = 0
        zero = 0
        for j in range(len(nums)):
            if nums[j] != 1:
                zero += 1
            while zero > k:
                if nums[i] == 0:
                    zero -= 1
                i+=1
            l = j - i + 1
            maxLen = max(maxLen, l)
        return (maxLen)
