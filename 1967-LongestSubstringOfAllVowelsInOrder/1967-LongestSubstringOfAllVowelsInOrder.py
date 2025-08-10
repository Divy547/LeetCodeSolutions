# Last updated: 8/11/2025, 1:00:54 AM
class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        ranks = {'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5}
        max_len = 0
        unique_vowels = 1
        prevRank = 1
        j = 0
        while j < len(word) and word[j] != "a":
            j += 1
        if j == len(word):
            return 0 
        i = j
        
        for j in range(len(word)):
            currRank = ranks[word[j]]
            if currRank < prevRank:
                i = j
                unique_vowels = 1
            
            elif currRank > prevRank:
                unique_vowels += 1
            
            prevRank = currRank
            if unique_vowels == 5:
                max_len = max(max_len, j - i + 1)
        
        return max_len
