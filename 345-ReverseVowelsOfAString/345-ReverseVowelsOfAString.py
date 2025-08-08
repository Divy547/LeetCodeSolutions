# Last updated: 8/9/2025, 2:26:55 AM
class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        i = 0
        j = len(s) - 1
        vowels = "aeiouAEIOU"
        while i <= j:
            if s[i] in vowels and s[j] in vowels:
                temp = s[i]
                s[i] = s[j]
                s[j] = temp
                i+=1
                j-=1
            elif s[j] not in vowels:
                j-=1
            elif s[i] not in vowels:
                i+=1
        return "".join(s)