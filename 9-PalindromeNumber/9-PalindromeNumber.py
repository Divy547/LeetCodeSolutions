# Last updated: 9/4/2025, 3:01:49 PM
class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        y = x
        rev = 0
        while x:
            a = x % 10
            rev = rev*10+a
            x = x // 10
        return  rev == y
        