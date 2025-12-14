# Last updated: 12/14/2025, 8:07:38 AM
1class Solution:
2    def absDifference(self, nums: List[int], k: int) -> int:
3        numbers = sorted(nums)
4        return abs(sum(numbers[-1:-k-1:-1]) - sum(numbers[0:k]))