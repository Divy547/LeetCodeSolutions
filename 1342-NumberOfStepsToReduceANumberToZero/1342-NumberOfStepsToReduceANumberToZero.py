# Last updated: 10/29/2026, 9:35:49 PM
class Solution(object):
    def numberOfSteps(self, num):
        count = 0
        while num != 0:
            if (num % 2) == 0:
                num /=2
            else:
                num -= 1
            count +=1 
            
        return count