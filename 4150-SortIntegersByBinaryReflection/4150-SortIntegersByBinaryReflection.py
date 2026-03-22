# Last updated: 3/22/2026, 10:33:03 PM
class Solution:
    def sortByReflection(self, nums: List[int]) -> List[int]:
        def ref(x):
            b = bin(x)[2::]
            rb = b[::-1]
            return int(rb, 2)
        return sorted(nums, key=lambda x : (ref(x),x))
            