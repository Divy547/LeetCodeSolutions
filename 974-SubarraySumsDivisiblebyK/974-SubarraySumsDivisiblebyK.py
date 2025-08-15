# Last updated: 8/15/2025, 11:01:25 PM
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum=0
        count=0
        freq={0:1}
        for num in nums:
            prefix_sum+=num
            rem=prefix_sum%k
            
            if rem in freq:
                count+=freq[rem]
                freq[rem]+=1
            else:
                freq[rem]=1
        return count
