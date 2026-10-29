# Last updated: 10/29/2026, 9:36:18 PM
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(0, len(nums)):
            nums[i] = nums[i]**2
        nums.sort()
        return nums