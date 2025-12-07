# Last updated: 12/7/2025, 8:16:16 AM
1class Solution:
2    def sortByReflection(self, nums: List[int]) -> List[int]:
3        def ref(x):
4            b = bin(x)[2::]
5            rb = b[::-1]
6            return int(rb, 2)
7        return sorted(nums, key=lambda x : (ref(x),x))
8            