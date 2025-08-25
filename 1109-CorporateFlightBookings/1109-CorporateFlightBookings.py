# Last updated: 8/25/2025, 11:16:19 PM
class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        diff = [0]*(len(s)+1)
        for l, r, direction in shifts:
                if direction == 1:
                    diff[l] += 1
                    diff[r+1] -= 1
                else:
                    diff[l] -= 1
                    diff[r+1] += 1
        for i in range(1, len(diff)):
            diff[i] = diff[i-1] + diff[i]
        print(diff[:-1])
        res = []
        for i, ch in enumerate(s):
            base = ord('a')
            oldval = ord(ch) - base
            newVal = (oldval + diff[i]) % 26
            res.append(chr(base + newVal))
        return "".join(res)