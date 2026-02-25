# Last updated: 2/25/2026, 11:22:58 AM
1class Solution:
2    def canJump(self, nums: List[int]) -> bool:
3        reach = 0
4        for i in range(len(nums)):
5            if i > reach:
6                return False
7            reach = max(reach, i + nums[i])
8        return True