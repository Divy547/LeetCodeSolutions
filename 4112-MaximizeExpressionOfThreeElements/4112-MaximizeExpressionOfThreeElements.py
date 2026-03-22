# Last updated: 3/22/2026, 10:33:04 PM
class Solution:
    def maximizeExpressionOfThree(self, nums: List[int]) -> int:
        nums.sort()
        
        return nums[-1] + nums[-2] - nums[0]
        