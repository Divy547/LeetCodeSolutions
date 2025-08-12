# Last updated: 8/12/2025, 11:02:45 PM
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1:
            return True
        if n < 1:
            return False
        return self.isPowerOfFour(n/4)