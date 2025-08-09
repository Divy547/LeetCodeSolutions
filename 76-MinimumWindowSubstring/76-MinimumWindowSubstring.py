# Last updated: 8/10/2025, 2:47:57 AM
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter

        i = 0
        target = Counter(t)
        window = {}
        res = [0, 0]
        minLen = float('inf')
        currChar, targetChar = 0, len(target)
        for j in range(len(s)):
            window[s[j]] = window.get(s[j], 0) + 1

            if s[j] in target and window[s[j]] == target[s[j]]:
                currChar += 1

            while currChar == targetChar:
                if j - i + 1 < minLen:
                    res = [i, j]
                    minLen = j - i + 1
                window[s[i]] -=1
                if s[i] in target and window[s[i]] < target[s[i]]:
                    currChar -= 1
                i+=1
        start, end = res
        return s[start:end+1] if minLen != float('inf') else ""




