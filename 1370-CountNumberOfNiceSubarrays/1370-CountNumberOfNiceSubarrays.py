# Last updated: 8/19/2025, 11:43:31 PM
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        from collections import Counter
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i] = 0
            else:
                nums[i] = 1
        hashMap = defaultdict(int)
        hashMap[0] = 1
        count = 0
        currSum = 0
        for x in nums:
            currSum += x
            if currSum - k in hashMap:
                count += hashMap[currSum - k]
            hashMap[currSum] += 1
        return count