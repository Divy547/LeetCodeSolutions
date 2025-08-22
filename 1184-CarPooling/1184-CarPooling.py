# Last updated: 8/23/2025, 12:00:21 AM
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        changes = {}
        for num, start, end in trips:
            changes[start] = changes.get(start, 0) + num
            changes[end] = changes.get(end, 0) - num

        passengers = 0
        for loc in sorted(changes.keys()):
            passengers += changes[loc]
            if passengers > capacity:
                return False
        return True