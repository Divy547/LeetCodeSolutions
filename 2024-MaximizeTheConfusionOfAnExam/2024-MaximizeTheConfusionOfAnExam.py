# Last updated: 10/29/2026, 9:34:40 PM
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
