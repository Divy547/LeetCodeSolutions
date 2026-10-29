# Last updated: 10/29/2026, 9:36:20 PM
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
