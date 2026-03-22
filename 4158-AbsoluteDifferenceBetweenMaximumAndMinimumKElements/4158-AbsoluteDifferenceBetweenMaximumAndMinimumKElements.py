# Last updated: 3/22/2026, 10:33:07 PM
class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        numbers = sorted(nums)
        return abs(sum(numbers[-1:-k-1:-1]) - sum(numbers[0:k]))