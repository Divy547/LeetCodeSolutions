# Last updated: 8/9/2025, 2:26:59 AM
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        maxDeque = deque()
        res = []
        for j in range(len(nums)):
            while maxDeque and nums[j] > nums[maxDeque[-1]]:
                maxDeque.pop()
            maxDeque.append(j)
            if maxDeque[0] <= j-k:
                maxDeque.popleft()
            if j >= k - 1:
                res.append(nums[maxDeque[0]])
            
        return res