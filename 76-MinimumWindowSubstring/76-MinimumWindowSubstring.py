# Last updated: 8/10/2025, 2:32:12 AM
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        i = 0
        window = Counter()
        target = Counter(t)
        minLen = float('inf')
        startIndex = 0

        for j in range(len(s)):
            window[s[j]] += 1
            while all(window[c] >= target[c] for c in target):
                if j - i + 1 < minLen:
                    minLen = j - i + 1
                    startIndex = i
                window[s[i]] -= 1
                i+=1
            
        if minLen != float('inf'):
            return s[startIndex:startIndex + minLen]
        else:
            return ""

