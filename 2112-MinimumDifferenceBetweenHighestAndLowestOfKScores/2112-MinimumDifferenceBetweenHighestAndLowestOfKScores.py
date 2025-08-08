# Last updated: 8/9/2025, 2:26:25 AM
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        #[1,4,7,9]
        minDif = float('inf')
        nums.sort()
        for i in range(len(nums) - k + 1):
            dif = nums[i+k-1] - nums[i]
            minDif = min(dif, minDif)
        return minDif