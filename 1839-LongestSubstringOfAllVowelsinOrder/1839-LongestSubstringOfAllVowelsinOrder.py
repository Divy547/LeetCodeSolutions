# Last updated: 8/10/2025, 7:07:34 PM
class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        from collections import Counter
        if 'a' not in word:
            return 0

        ranks = {"a": 1, "e": 2, "i": 3, "o": 4, "u": 5}
        window = Counter()

        # Skip to first 'a'
        j = 0
        while j < len(word) and word[j] != "a":
            j += 1
        if j == len(word):
            return 0  # no 'a' found
        i = j
        prevRank = 1
        maxLen = 0

        for j in range(j, len(word)):
            c = word[j]
            if c not in ranks:
                # If character is not vowel, reset window
                window.clear()
                i = j + 1
                prevRank = 0
                continue

            currRank = ranks[c]
            window[c] += 1

            # If vowel order breaks, reset window to start at current char
            if currRank < prevRank:
                # Shrink window until next 'a' or reset fully if none found
                found_a = False
                while i <= j:
                    left_char = word[i]
                    window[left_char] -= 1
                    if window[left_char] == 0:
                        del window[left_char]
                    i += 1
                    if left_char == 'a':
                        found_a = True
                        break
                if not found_a:
                    window.clear()
                    prevRank = 0
                    i = j + 1
                    continue
                window = Counter({c: 1})
                i = j
                prevRank = currRank
            else:
                prevRank = currRank

            if all(window.get(v, 0) >= 1 for v in ranks):
                maxLen = max(maxLen, j - i + 1)

        return maxLen
