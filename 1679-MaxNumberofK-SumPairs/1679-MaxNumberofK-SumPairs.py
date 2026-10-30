# Last updated: 10/30/2026, 9:14:23 AM
1class Solution:
2    def maxOperations(self, nums: List[int], k: int) -> int:
3        nums.sort()
4        operations = 0
5        n = len(nums)
6        i = 0
7        j = n - 1
8        while i < j:
9            if(nums[i] + nums[j] < k):
10                print(nums[i], nums[j])
11                i+=1
12            elif (nums[i] + nums[j] > k):
13                print(nums[i], nums[j])
14                j-=1
15            
16            elif(nums[i] + nums[j] == k):
17                i+=1
18                j-=1
19                operations+=1
20                print(nums[i], nums[j])
21        return operations