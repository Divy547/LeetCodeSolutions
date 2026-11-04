# Last updated: 11/4/2026, 9:52:57 PM
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        n = len(s1)

        s1_count = [0] * 26
        window_count = [0] * 26

        # Build initial frequency arrays
        for i in range(n):
            s1_count[ord(s1[i]) - ord('a')] += 1
            window_count[ord(s2[i]) - ord('a')] += 1

        if s1_count == window_count:
            return True

        # Slide the window
        for right in range(n, len(s2)):

            # Add incoming character
            window_count[ord(s2[right]) - ord('a')] += 1

            # Remove outgoing character
            window_count[ord(s2[right - n]) - ord('a')] -= 1

            if s1_count == window_count:
                return True

        return False