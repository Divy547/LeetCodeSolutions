# Last updated: 8/27/2025, 11:00:17 PM
class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        MOD = 10**9 + 7
        freq = [0]*(len(nums)+1)
        for l, r in requests:
            freq[l] += 1
            if r + 1 < len(freq):
                freq[r + 1] -= 1
        for i in range(1, len(nums)):
            freq[i] += freq[i-1]

        freq = freq[:-1]

        nums.sort(reverse=True)
        freq.sort(reverse=True)

        ans = 0
        for a, b in zip(nums, freq):
            ans = (ans + a * b) % MOD

        return ans