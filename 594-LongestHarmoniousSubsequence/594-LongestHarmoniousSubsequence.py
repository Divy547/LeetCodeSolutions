# Last updated: 8/9/2025, 2:26:48 AM
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        #[1,2,2,2,3,3,5,7]
        maxLen = 0
        i = 0
        for j in range(len(nums)):
            while nums[j] - nums[i] > 1:
                i+=1
            if nums[j] - nums[i] == 1:
                maxLen = max(maxLen, j - i + 1)
        return maxLen