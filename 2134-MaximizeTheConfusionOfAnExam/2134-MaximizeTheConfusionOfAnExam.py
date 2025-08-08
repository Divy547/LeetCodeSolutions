# Last updated: 8/9/2025, 2:26:24 AM
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        from collections import defaultdict
        i = 0
        maxFreq = 0
        maxLen = 0
        dct = defaultdict(int)

        for j in range(len(answerKey)):
            dct[answerKey[j]] += 1
            maxFreq = max(maxFreq, dct[answerKey[j]])
            if (j - i + 1) - maxFreq > k:
                dct[answerKey[i]] -= 1
                i += 1

            maxLen = max(maxLen, j - i + 1)

        return maxLen
