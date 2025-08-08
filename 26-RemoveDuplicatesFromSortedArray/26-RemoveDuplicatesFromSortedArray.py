# Last updated: 8/9/2025, 2:27:21 AM
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for j in range(1, len(nums)):
            if  nums[i] != nums[j]:
                i+=1
                nums[i] = nums[j]
        return i + 1