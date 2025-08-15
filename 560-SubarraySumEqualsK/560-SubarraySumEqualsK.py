# Last updated: 8/15/2025, 10:38:19 PM
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        from collections import Counter
        count = 0
        hashMap = defaultdict(int)
        hashMap[0] = 1
        currSum = 0
        for x in nums:
            currSum += x
            if currSum - k in hashMap:
                count += hashMap[currSum - k]
            hashMap[currSum] += 1
        return count
        