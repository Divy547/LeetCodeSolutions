# Last updated: 11/4/2026, 9:52:08 PM
from collections import Counter
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        operations = 0
        n = len(nums)
        hashMap = Counter(nums)
        
        for num in hashMap:
            req = k - num
            if num == req :
                operations += hashMap[num] // 2

            elif hashMap[req] > 0:
                operations += min(hashMap[num], hashMap[req])
                hashMap[req] = 0
            hashMap[num] = 0
        return operations




        # Two pointers Approach
        # nums.sort()
        # i = 0
        # j = n - 1
        # while i < j:
        #     if nums[i] + nums[j] == k:
        #         i+=1
                
        #         operations+=1
            
        #     if(nums[i] + nums[j] < k):
        #         print(nums[i], nums[j])
        #         i+=1
        #     elif (nums[i] + nums[j] > k):
        #         print(nums[i], nums[j])
        #         j-=1
            
        #     elif(nums[i] + nums[j] == k):
               
        #         print(nums[i], nums[j])