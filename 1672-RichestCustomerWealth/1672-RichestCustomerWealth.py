# Last updated: 10/29/2026, 9:35:12 PM
class Solution(object):
    def maximumWealth(self, accounts):
        wealth = 0
        for i in range(0, len(accounts)):
            sum = 0
            for j in range(0, len(accounts[i])):
                sum += accounts[i][j]
                wealth = max(wealth, sum)
        return wealth