# Last updated: 8/9/2025, 2:26:52 AM
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict
        i = 0
        maxFreq = 0
        maxLen = 0
        dct = defaultdict(int)

        for j in range(len(s)):
            dct[s[j]] += 1
            maxFreq = max(maxFreq, dct[s[j]])
            if (j - i + 1) - maxFreq > k:
                dct[s[i]] -= 1
                i += 1

            maxLen = max(maxLen, j - i + 1)

        return maxLen
        
            
