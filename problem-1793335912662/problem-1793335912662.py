# Last updated: 10/30/2026, 10:21:52 AM
1class Solution:
2    def dividePlayers(self, skill: list[int]) -> int:
3        skill.sort()
4        n = len(skill)
5        reqSkill = skill[0] + skill[n-1]
6        j = n - 1
7        chemistry = 0
8        i = 0
9        while i < j:
10            if skill[i] + skill[j] == reqSkill:
11                print(skill[i], skill[j])
12                chemistry += skill[i]*skill[j]
13                i+=1 
14                j-=1
15            else:
16                return -1
17        return chemistry
18
19