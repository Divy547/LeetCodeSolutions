# Last updated: 10/29/2026, 11:29:49 PM
1class Solution:
2    def numRescueBoats(self, people: list[int], limit: int) -> int:
3        people.sort()
4        boats = 0
5        n = len(people)
6        j = n - 1
7        i = 0
8        while i <= j:
9            boats += 1
10
11            if people[i] + people[j] <= limit:
12                i += 1
13
14            j -= 1
15                            
16        return boats
17
18                