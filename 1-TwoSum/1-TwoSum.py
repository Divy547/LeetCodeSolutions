# Last updated: 8/9/2025, 2:27:35 AM
class Solution(object):
    def twoSum(self, nums, target):
        hashMap = {}
        for i in range(0, len(nums)):
            if target - nums[i] in hashMap and hashMap[target - nums[i]] != i:
                return [hashMap[target - nums[i]], i]
            else:
                hashMap[nums[i]] = i
            
            # for j in range(0, len(nums)):
            #     if(nums[i] + nums[j] == target and i != j):
            #         return [i, j]
        