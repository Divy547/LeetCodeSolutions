# Last updated: 8/13/2025, 12:13:49 AM
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        from collections import Counter
        maxLen = 0
        for targetUnique in range(1, 27):
            i = 0
            window = Counter()
            uniqueChars = 0
            charsAtLeastK = 0  
            for j in range(len(s)):
                window[s[j]] += 1
                if window[s[j]] == 1:
                    uniqueChars += 1
                if window[s[j]] == k:
                    charsAtLeastK += 1
                while uniqueChars > targetUnique:
                    if window[s[i]] == k:
                        charsAtLeastK -= 1
                    window[s[i]] -= 1
                    if window[s[i]] == 0:
                        uniqueChars -= 1
                        del window[s[i]]
                    i += 1

                if uniqueChars == targetUnique and uniqueChars == charsAtLeastK:
                    maxLen = max(maxLen, j - i + 1)

                    
        return maxLen