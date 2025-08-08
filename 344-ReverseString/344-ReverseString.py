# Last updated: 8/9/2025, 2:26:57 AM
class Solution:
    def reverseString(self, s: List[str]) -> None:
        
        slow = 0
        fast = len(s) - 1
        while slow < fast:
            temp = s[slow]
            s[slow] = s[fast]
            s[fast] = temp
            slow+=1
            fast-=1
        