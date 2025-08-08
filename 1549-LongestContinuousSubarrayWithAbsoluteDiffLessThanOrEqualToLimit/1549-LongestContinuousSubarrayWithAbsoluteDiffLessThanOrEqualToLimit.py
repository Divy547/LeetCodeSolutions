# Last updated: 8/9/2025, 2:26:35 AM
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        from collections import deque
        i = 0
        minDq = deque()
        maxDq = deque()
        maxLen = 0
        
        for j in range(len(nums)):
            while minDq and nums[j] < nums[minDq[-1]]:
                minDq.pop()
            minDq.append(j)
            while maxDq and nums[j] > nums[maxDq[-1]]:
                maxDq.pop()
            maxDq.append(j)
            
            while nums[maxDq[0]] - nums[minDq[0]] > limit:
                i+=1
                if minDq[0] < i:
                    minDq.popleft()
                if maxDq[0] < i:
                    maxDq.popleft()

            maxLen = max(maxLen, j - i + 1)
        return maxLen