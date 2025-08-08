# Last updated: 8/9/2025, 2:26:58 AM
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        val = 0
        i = 0
        for j in range(0, len(nums)):
            if nums[i] == val and nums[j] != val:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                i+=1
            elif nums[i] != val:
                i+=1    
        return nums
        