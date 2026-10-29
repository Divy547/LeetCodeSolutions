# Last updated: 10/29/2026, 9:34:51 PM
class Solution(object):
    def findMiddleIndex(self, nums):
        for i in range(0, len(nums)):
            rsum = 0
            lsum = 0
            for j in range(0, i):
                lsum += nums[j]
            for j in range(i + 1, len(nums)):
                rsum += nums[j]
            if rsum == lsum:
                return i
        
        return -1
        