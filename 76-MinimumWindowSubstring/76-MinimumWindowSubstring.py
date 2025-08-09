# Last updated: 8/10/2025, 2:50:18 AM
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        # ASCII size (256 is safe for extended ASCII)
        target = [0] * 256
        window = [0] * 256
        
        # Fill target counts
        for c in t:
            target[ord(c)] += 1
        
        need = sum(1 for count in target if count > 0)  # unique chars needed
        have = 0
        
        res = [0, 0]
        minLen = float('inf')
        i = 0
        
        for j in range(len(s)):
            c_j = ord(s[j])
            window[c_j] += 1
            
            if target[c_j] > 0 and window[c_j] == target[c_j]:
                have += 1
            
            # Shrink window from left when valid
            while have == need:
                if j - i + 1 < minLen:
                    minLen = j - i + 1
                    res = [i, j]
                
                c_i = ord(s[i])
                window[c_i] -= 1
                if target[c_i] > 0 and window[c_i] < target[c_i]:
                    have -= 1
                i += 1
        
        start, end = res
        return s[start:end+1] if minLen != float('inf') else ""




