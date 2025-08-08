# Last updated: 8/9/2025, 2:26:22 AM
class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        unplaced = 0
        used = set()
        for i in range(0, n):
            j = 0
            placed = False
            while j < n:
                if fruits[i] <= baskets[j] and j not in used:
                    used.add(j) 
                    placed = True 
                    break
                j+=1
            if not placed:
                unplaced += 1
        return unplaced
            