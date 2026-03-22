# Last updated: 3/22/2026, 10:33:08 PM
class Solution:
    def minLengthAfterRemovals(self, s: str) -> int:
        a = s.count('a')
        b = s.count('b')
        return abs(a-b)