# Last updated: 8/10/2025, 7:11:49 PM
class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        ranks = {'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5}
        i = 0
        max_len = 0
        unique_vowels = 1
        prevRank = 1
        j = 0
        while j < len(word) and word[j] != "a":
            j += 1
        if j == len(word):
            return 0  # no 'a' found
        i = j
        
        for j in range(len(word)):
            currRank = ranks[word[j]]
            if currRank < prevRank:
                i = j
                unique_vowels = 1
            
            # If rank increased, means we found a new vowel in order
            elif currRank > prevRank:
                unique_vowels += 1
            
            prevRank = currRank
            
            # Update max length only if all vowels found
            if unique_vowels == 5:
                max_len = max(max_len, j - i + 1)
        
        return max_len
