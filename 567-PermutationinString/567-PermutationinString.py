# Last updated: 10/31/2026, 9:23:21 PM
1class Solution:
2    def checkInclusion(self, s1: str, s2: str) -> bool:
3
4        if len(s1) > len(s2):
5            return False
6
7        n = len(s1)
8
9        s1_count = [0] * 26
10        window_count = [0] * 26
11
12        # Build initial frequency arrays
13        for i in range(n):
14            s1_count[ord(s1[i]) - ord('a')] += 1
15            window_count[ord(s2[i]) - ord('a')] += 1
16
17        if s1_count == window_count:
18            return True
19
20        # Slide the window
21        for right in range(n, len(s2)):
22
23            # Add incoming character
24            window_count[ord(s2[right]) - ord('a')] += 1
25
26            # Remove outgoing character
27            window_count[ord(s2[right - n]) - ord('a')] -= 1
28
29            if s1_count == window_count:
30                return True
31
32        return False