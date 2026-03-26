# Last updated: 3/26/2026, 6:28:01 PM
1class Solution:
2    def containsDuplicate(self, nums: List[int]) -> bool:
3        a = set(nums)
4        return False if len(a) == len(nums) else True