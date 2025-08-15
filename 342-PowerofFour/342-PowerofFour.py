# Last updated: 8/15/2025, 9:40:01 PM
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1:
            return True
        if n < 1 or n % 4!= 0:
            return False
        return self.isPowerOfFour(n//4)