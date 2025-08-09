# Last updated: 8/10/2025, 3:13:51 AM
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        if n < 1:
            return False
        return self.isPowerOfTwo(n/2)