# Last updated: 3/22/2026, 10:33:06 PM
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
            