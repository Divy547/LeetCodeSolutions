# Last updated: 10/29/2026, 9:33:57 PM
class Solution:
    def reverseWords(self, s: str) -> str:
        def vowelCount(w):
            count = 0
            for ch in w:
                if ch in "aeiou":
                    count+=1
            return count
        words = s.split()
        currentCount = vowelCount(words[0])
        for i in range(1, len(words)):
            if vowelCount(words[i]) == currentCount:
                words[i] = words[i][::-1]
                currentCount = vowelCount(words[i])
        
           
            
        return " ".join(words)
            