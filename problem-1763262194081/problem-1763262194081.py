# Last updated: 11/16/2025, 8:33:14 AM
class Solution:
    def minLengthAfterRemovals(self, s: str) -> int:
        a = s.count('a')
        b = s.count('b')
        return abs(a-b)