# Last updated: 11/3/2026, 9:46:13 PM
1
2class Solution:
3    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
4        seen = set()
5        left = 0
6        curr_sum = 0
7        ans = 0
8
9        for right in range(len(nums)):
10            # Remove duplicates from the current window
11            while nums[right] in seen:
12                seen.remove(nums[left])
13                curr_sum -= nums[left]
14                left += 1
15
16            # Add current element
17            seen.add(nums[right])
18            curr_sum += nums[right]
19
20            # Maintain window size k
21            if right - left + 1 > k:
22                seen.remove(nums[left])
23                curr_sum -= nums[left]
24                left += 1
25
26            # Check valid window
27            if right - left + 1 == k:
28                ans = max(ans, curr_sum)
29
30        return ans
31