# Last updated: 8/15/2025, 10:59:06 PM
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        hashMap = {0:1}
        count = 0
        currSum = 0
        for x in nums:
            currSum += x
            remainder = currSum % k
            if remainder < 0:
                remainder += k 
            if remainder in hashMap:
                count += hashMap[remainder]
            if remainder in hashMap:
                hashMap[remainder] += 1
            else:
                hashMap[remainder] = 1
        return count
