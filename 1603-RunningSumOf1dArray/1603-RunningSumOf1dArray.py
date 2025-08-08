# Last updated: 8/9/2025, 2:26:33 AM
class Solution(object):
    def runningSum(self, nums):
        for i in range(1,len(nums)):
            nums[i]+=nums[i-1]
        return nums
        