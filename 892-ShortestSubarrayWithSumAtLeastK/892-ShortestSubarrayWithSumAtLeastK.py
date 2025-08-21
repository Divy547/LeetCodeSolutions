# Last updated: 8/22/2025, 1:06:24 AM
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix = [0]*(len(nums) + 1)
        for i in range(len(nums)):
            prefix[i + 1] = prefix[i] + nums[i]
        res = n + 1
        dq = deque()
        
        for j in range(n + 1):
            
            while dq and prefix[j] - prefix[dq[0]] >= k:
                res = min(res, j - dq.popleft())
            
            # maintain increasing order of prefix sums
            while dq and prefix[j] <= prefix[dq[-1]]:
                dq.pop()
            
            dq.append(j)
        return res if res <= n else -1