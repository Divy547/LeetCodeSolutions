# Last updated: 8/9/2025, 2:26:20 AM
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        window = []
        for j in range(0, len(s)):
            window.append(s[j])
            if len(window) > 3:
                window.pop(0)
            if len(window) == 3 and len(set(window)) == 3:
                count+=1
        return count
            
            
            
            
        