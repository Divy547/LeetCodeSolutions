# Last updated: 8/22/2025, 1:06:32 AM
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        from collections import Counter
        hashMap = {0:-1}
        currSum = 0

        for i in range(len(nums)):
            currSum += nums[i]
            if currSum % k in hashMap:
                if i - hashMap[currSum % k] >= 2:
                    return True
            else:
                hashMap[currSum % k] = i
        return False