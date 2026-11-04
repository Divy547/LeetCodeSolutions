# Last updated: 11/4/2026, 9:51:42 PM
class Solution:
    def dividePlayers(self, skill: list[int]) -> int:
        skill.sort()
        n = len(skill)
        reqSkill = skill[0] + skill[n-1]
        j = n - 1
        chemistry = 0
        i = 0
        while i < j:
            if skill[i] + skill[j] == reqSkill:
                print(skill[i], skill[j])
                chemistry += skill[i]*skill[j]
                i+=1 
                j-=1
            else:
                return -1
        return chemistry

