# Last updated: 10/29/2026, 9:34:00 PM
class Solution:
    def minLengthAfterRemovals(self, s: str) -> int:
        a = s.count('a')
        b = s.count('b')
        return abs(a-b)