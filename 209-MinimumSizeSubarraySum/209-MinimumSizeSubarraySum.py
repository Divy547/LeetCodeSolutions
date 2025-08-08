# Last updated: 8/9/2025, 2:27:02 AM
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        lenMin = len(nums) + 1
        
        total = 0
        i = 0
        for j in range(0, len(nums)):
            total += nums[j]
            while total >= target:
                lenMin = min(lenMin, j-i + 1)
                total -= nums[i]
                i+=1
            
        return 0 if lenMin == len(nums) + 1 else lenMin

            

    