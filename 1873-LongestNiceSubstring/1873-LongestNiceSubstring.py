# Last updated: 8/9/2025, 2:26:27 AM
class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) < 2:
            return ""

        charset = set(s)

        for i in range(len(s)):
            if s[i].swapcase() not in charset:
                left = self.longestNiceSubstring(s[:i])
                right = self.longestNiceSubstring(s[i+1:])
                return left if len(left) >= len(right) else right

        return s
