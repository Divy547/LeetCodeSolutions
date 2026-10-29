# Last updated: 10/29/2026, 9:36:02 PM
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        i = 0
        maxLen = 0
        currCost = 0
        for j in range(len(s)):
            currCost += abs(ord(s[j]) - ord(t[j]))
            while currCost > maxCost:
                currCost -= abs(ord(s[i]) - ord(t[i]))
                i+=1
            maxLen = max(maxLen, j - i + 1)
        return maxLen