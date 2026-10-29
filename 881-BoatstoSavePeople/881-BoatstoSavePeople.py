# Last updated: 10/29/2026, 11:28:32 PM
1class Solution:
2    def numRescueBoats(self, people: list[int], limit: int) -> int:
3        people.sort()
4        boats = 0
5        n = len(people)
6        j = n - 1
7        i = 0
8        while i <= j:
9            boats += 1
10            if people[j] >= limit:
11                j -= 1
12            elif people[i] + people[j] > limit:
13                j-=1
14                
15            elif people[i] + people[j] <= limit:
16                i += 1
17                j -= 1
18                    
19        return boats
20
21                