# Last updated: 8/9/2025, 2:27:26 AM
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(0, len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            a = nums[i]
            k = i + 1
            j = len(nums) - 1
            while k < j:
                total = a + nums[k] + nums[j]
                if total == 0:
                    res.append([nums[i], nums[k], nums[j]])
                    while k < j and nums[k] == nums[k + 1]:
                        k += 1
                    while k < j and nums[j] == nums[j - 1]:
                        j -= 1
                    k += 1
                    j -= 1
                elif total > 0:
                    j -= 1
                else:
                    k += 1
        return res
