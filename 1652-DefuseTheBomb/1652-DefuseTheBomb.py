# Last updated: 10/29/2026, 9:35:18 PM
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