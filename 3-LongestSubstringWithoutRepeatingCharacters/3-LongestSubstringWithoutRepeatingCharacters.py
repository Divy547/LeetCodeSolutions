# Last updated: 8/9/2025, 2:27:32 AM
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        hashMap = set()
        maxLen = 0
        i = 0
        j = 0
        for j in range(0, len(s)):
            while s[j] in hashMap:
                hashMap.remove(s[i])
                i+=1
            hashMap.add(s[j])
            maxLen = max(maxLen, j - i + 1)
            
        return maxLen