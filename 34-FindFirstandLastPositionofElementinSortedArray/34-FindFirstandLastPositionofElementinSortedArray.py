# Last updated: 11/9/2026, 10:20:40 PM
1class Solution:
2    def searchRange(self, nums: List[int], target: int) -> List[int]:
3
4        def binarySearch(findFirst):
5            left, right = 0, len(nums) - 1
6            ans = -1
7
8            while left <= right:
9                mid = (left + right) // 2
10
11                if nums[mid] == target:
12                    ans = mid
13
14                    if findFirst:
15                        right = mid - 1
16                    else:
17                        left = mid + 1
18
19                elif nums[mid] < target:
20                    left = mid + 1
21                else:
22                    right = mid - 1
23
24            return ans
25
26        return [binarySearch(True), binarySearch(False)]