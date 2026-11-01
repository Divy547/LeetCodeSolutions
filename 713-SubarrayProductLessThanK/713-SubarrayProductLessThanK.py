# Last updated: 11/1/2026, 10:49:14 PM
1
2class Solution:
3    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
4        if k <= 1:
5            return 0
6
7        left = 0
8        product = 1
9        count = 0
10
11        for right in range(len(nums)):
12            product *= nums[right]
13
14            while product >= k:
15                product //= nums[left]
16                left += 1
17
18            count += right - left + 1
19
20        return count
21