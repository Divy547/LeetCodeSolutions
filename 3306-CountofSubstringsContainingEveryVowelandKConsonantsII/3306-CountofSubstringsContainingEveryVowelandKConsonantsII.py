# Last updated: 11/6/2026, 10:34:06 PM
1class Solution:
2    def countOfSubstrings(self, word: str, k: int) -> int:
3        vowels = set("aeiou")
4
5        def atMost(k):
6            if k < 0:
7                return 0
8
9            left = 0
10            consonants = 0
11            last = {v: -1 for v in vowels}
12            count = 0
13
14            for right, ch in enumerate(word):
15                if ch in vowels:
16                    last[ch] = right
17                else:
18                    consonants += 1
19
20                while consonants > k:
21                    if word[left] not in vowels:
22                        consonants -= 1
23                    left += 1
24
25                min_last = min(last.values())
26
27                if min_last >= left:
28                    count += min_last - left + 1
29
30            return count
31
32        return atMost(k) - atMost(k - 1)