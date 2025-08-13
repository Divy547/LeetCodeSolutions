# Last updated: 8/13/2025, 10:42:33 PM
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m = nums[0]
        c = 0
        for x in nums:
            if c == 0 :
                m = x
                c = 1
            elif m == x:
                c += 1
            else:
                c -= 1
        return m