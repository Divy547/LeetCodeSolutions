# Last updated: 10/29/2026, 9:33:58 PM
class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        numbers = sorted(nums)
        return abs(sum(numbers[-1:-k-1:-1]) - sum(numbers[0:k]))