# Last updated: 8/9/2025, 2:27:08 AM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # i = 0
        # j = 1
        # maxProfit = 0
        # while j < len(prices):
        #     if prices[j] > prices[i]:
        #         profit = prices[j] - prices[i]
        #         maxProfit = max(maxProfit, profit)
        #     else:
        #         i = j
        #     j+=1
        dp = [0]*len(prices)
        minPrice = prices[0]
        for i in range(1, len(prices)):
            minPrice = min(minPrice, prices[i])
            dp[i] = max(dp[i - 1], prices[i] - minPrice)
        return dp[-1]
