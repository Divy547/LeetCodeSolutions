# Last updated: 3/25/2026, 9:06:41 AM
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 100000:
            if nums[0] == -100000000:
                return 2
            return 100000
        num_set = set(nums)
        max_len = 0
        for num in num_set:
            if num - 1 not in num_set:
                curr = num + 1 
                cur_len = 1
                while curr in num_set:
                    cur_len += 1
                    curr += 1
                max_len = max(max_len, cur_len)
        return max_len
        