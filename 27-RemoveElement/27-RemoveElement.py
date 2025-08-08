# Last updated: 8/9/2025, 2:27:20 AM
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        i = 0
        for j in range(0, len(nums)):
            if nums[i] == val and nums[j] != val:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                i+=1
            elif nums[i] != val:
                i+=1
        return i