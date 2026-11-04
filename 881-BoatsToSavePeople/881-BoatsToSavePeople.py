# Last updated: 11/4/2026, 9:52:38 PM
class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        people.sort()
        boats = 0
        n = len(people)
        j = n - 1
        i = 0
        while i <= j:
            boats += 1

            if people[i] + people[j] <= limit:
                i += 1

            j -= 1
                            
        return boats

                