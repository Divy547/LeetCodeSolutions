# Last updated: 10/29/2026, 9:33:55 PM
class Solution:
    def sortByReflection(self, nums: List[int]) -> List[int]:
        def ref(x):
            b = bin(x)[2::]
            rb = b[::-1]
            return int(rb, 2)
        return sorted(nums, key=lambda x : (ref(x),x))
            