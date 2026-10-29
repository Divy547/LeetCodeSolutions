# Last updated: 10/29/2026, 9:35:09 PM
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        hashMap = {}
        j = 0
        i = 0
        score = 0
        maxScore = 0
        for j in range(0, len(nums)):
            while nums[j] in hashMap:
                hashMap.pop(nums[i])
                score -= nums[i]
                i += 1
            hashMap[nums[j]] = j
            score += nums[j]
            maxScore = max(maxScore, score)
        return maxScore