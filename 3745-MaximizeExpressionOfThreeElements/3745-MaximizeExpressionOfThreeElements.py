# Last updated: 10/29/2026, 9:33:53 PM
class Solution:
    def maximizeExpressionOfThree(self, nums: List[int]) -> int:
        nums.sort()
        
        return nums[-1] + nums[-2] - nums[0]
        