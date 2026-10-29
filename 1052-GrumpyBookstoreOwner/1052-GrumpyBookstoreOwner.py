# Last updated: 10/29/2026, 9:36:11 PM
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        curSat = 0
        maxSat = 0
        i = 0
        currCust = 0
        for j in range(len(customers)):
            if grumpy[j] == 0:
                curSat += customers[j]

        for j in range(len(customers)):
            if grumpy[j] == 1:
                currCust += customers[j]
            
            if j >= minutes - 1:
                maxSat = max(maxSat, currCust)
                if grumpy[i] == 1:
                    currCust -= customers[i]
                i+=1
        return curSat + maxSat