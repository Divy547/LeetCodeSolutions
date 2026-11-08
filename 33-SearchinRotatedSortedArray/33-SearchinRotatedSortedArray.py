# Last updated: 11/8/2026, 11:19:03 PM
1
2class Solution:
3    def search(self, nums: List[int], target: int) -> int:
4        left, right = 0, len(nums) - 1
5
6        while left <= right:
7            mid = (left + right) // 2
8
9            if nums[mid] == target:
10                return mid
11
12            # Left half is sorted
13            if nums[left] <= nums[mid]:
14                if nums[left] <= target < nums[mid]:
15                    right = mid - 1
16                else:
17                    left = mid + 1
18
19            # Right half is sorted
20            else:
21                if nums[mid] < target <= nums[right]:
22                    left = mid + 1
23                else:
24                    right = mid - 1
25
26        return -1
27