# Last updated: 10/30/2026, 9:51:54 AM
1from collections import Counter
2class Solution:
3    def maxOperations(self, nums: List[int], k: int) -> int:
4        operations = 0
5        n = len(nums)
6        hashMap = Counter(nums)
7        
8        for num in hashMap:
9            req = k - num
10            if num == req :
11                operations += hashMap[num] // 2
12
13            elif hashMap[req] > 0:
14                operations += min(hashMap[num], hashMap[req])
15                hashMap[req] = 0
16            hashMap[num] = 0
17        return operations
18
19
20
21
22        # Two pointers Approach
23        # nums.sort()
24        # i = 0
25        # j = n - 1
26        # while i < j:
27        #     if nums[i] + nums[j] == k:
28        #         i+=1
29                
30        #         operations+=1
31            
32        #     if(nums[i] + nums[j] < k):
33        #         print(nums[i], nums[j])
34        #         i+=1
35        #     elif (nums[i] + nums[j] > k):
36        #         print(nums[i], nums[j])
37        #         j-=1
38            
39        #     elif(nums[i] + nums[j] == k):
40               
41        #         print(nums[i], nums[j])