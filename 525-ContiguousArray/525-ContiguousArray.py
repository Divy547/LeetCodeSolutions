# Last updated: 8/15/2025, 11:42:10 PM
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        hashMap = {0:-1}
        nums = [-1 if x == 0 else 1 for x in nums]
        maxLen = 0
        currSum = 0
        for i, x in enumerate(nums):
            currSum += x
            if currSum in hashMap:
                maxLen = max(maxLen, i - hashMap[currSum])
            else:
                hashMap[currSum] = i
        return maxLen