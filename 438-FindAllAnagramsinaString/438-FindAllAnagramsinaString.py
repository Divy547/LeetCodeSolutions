# Last updated: 8/10/2025, 12:59:28 AM
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        from collections import Counter
        i = 0
        hashMap = set()
        res = []
        target = Counter(p)
        window = Counter()

        for j in range(len(s)):
            window[s[j]] += 1
            if j >= len(p):
                left_char = s[j - len(p)]
                if window[left_char] == 1:
                    del window[left_char]
                else:
                    window[left_char] -= 1
            if window == target:
                res.append(j-len(p)+1)
        return res

                