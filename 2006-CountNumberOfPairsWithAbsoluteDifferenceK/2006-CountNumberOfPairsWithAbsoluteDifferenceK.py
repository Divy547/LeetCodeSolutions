# Last updated: 10/29/2026, 9:34:45 PM
class Solution:
    def countKDifference(self, nums: list[int], k: int) -> int:
        i = 0
        count = 0
        while(i <= len(nums)):
            j = i + 1
            while(i < j and j < len(nums)):
                if(abs(nums[i] - nums[j]) == k):
                    count+=1
                j+=1
            i+=1
        return count