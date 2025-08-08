# Last updated: 8/9/2025, 2:26:31 AM
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k == 0:
            return [0]*len(code)
        elif k > 0:
            res = []
            for i in range(len(code)):
                sum = 0
                for j in range(i + 1, i + k + 1):
                    if j >= len(code):
                        sum += code[abs(len(code) - j)]
                    else:
                        sum += code[j]
                res.append(sum)
            return res
        elif k < 0:
            res = []
            for i in range(len(code)):
                sum = 0
                for j in range(i - 1, k-1+i, -1):
                    if j >= len(code):
                        sum += code[abs(len(code) - j)]
                    else:
                        sum += code[j]
                res.append(sum)
            return res