# Last updated: 12/14/2025, 8:25:49 AM
1class Solution:
2    def reverseWords(self, s: str) -> str:
3        def vowelCount(w):
4            count = 0
5            for ch in w:
6                if ch in "aeiou":
7                    count+=1
8            return count
9        words = s.split()
10        currentCount = vowelCount(words[0])
11        for i in range(1, len(words)):
12            if vowelCount(words[i]) == currentCount:
13                words[i] = words[i][::-1]
14                currentCount = vowelCount(words[i])
15        
16           
17            
18        return " ".join(words)
19            