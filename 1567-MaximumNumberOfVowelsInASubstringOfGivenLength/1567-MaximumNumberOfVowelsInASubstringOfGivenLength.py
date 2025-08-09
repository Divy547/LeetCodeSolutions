# Last updated: 8/10/2025, 12:13:46 AM
class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        vowels = "aeiou"
        maxCount = 0
        currCount = 0
        i = 0
        for j in range(len(s)):
            if s[j] in vowels:
                currCount += 1
            if j > k - 1:
                if s[i] in vowels:
                    currCount -= 1
                i+=1
            if j - i + 1 == k:
                maxCount = max(maxCount, currCount)
        return maxCount
