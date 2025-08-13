# Last updated: 8/13/2025, 10:40:14 PM
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        def majority(low, high):
            if low == high:
                return nums[low]

            mid = (low + high) // 2
            left_major = majority(low, mid)
            right_major = majority(mid + 1, high)

            if left_major == right_major:
                return left_major

            left_count = sum(1 for i in range(low, high + 1) if nums[i] == left_major)
            right_count = sum(1 for i in range(low, high + 1) if nums[i] == right_major)

            return left_major if left_count > right_count else right_major

        return majority(0, len(nums) - 1)