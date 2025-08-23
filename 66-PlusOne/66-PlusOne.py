# Last updated: 8/23/2025, 9:42:09 PM
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int("".join(map(str, digits)))
        num += 1
        return [int(d) for d in str(num)]