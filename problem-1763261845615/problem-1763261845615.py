# Last updated: 11/16/2025, 8:27:25 AM
class Solution:
    def maximizeExpressionOfThree(self, nums: List[int]) -> int:
        nums.sort()
        
        return nums[-1] + nums[-2] - nums[0]
        