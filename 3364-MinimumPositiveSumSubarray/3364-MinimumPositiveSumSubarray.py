# Last updated: 8/10/2025, 2:07:53 AM
class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        minSum = float('inf')

        for i in range(len(nums)):
            currSum = 0
            for j in range(i , len(nums)):
                currSum += nums[j]
                if l <= j - i + 1 <= r and currSum > 0:
                    minSum = min(minSum, currSum)
            
        if minSum != float('inf'):
            return minSum
        else:
            return -1
            