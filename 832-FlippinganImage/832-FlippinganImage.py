# Last updated: 8/29/2025, 11:06:23 PM
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in image:
            n = len(row)
            for i in range((n + 1) // 2):
                # flip + invert simultaneously
                row[i], row[n - 1 - i] = row[n - 1 - i] ^ 1, row[i] ^ 1
        return image

               


