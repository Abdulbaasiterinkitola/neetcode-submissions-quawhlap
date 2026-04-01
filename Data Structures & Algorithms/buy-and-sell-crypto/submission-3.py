class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, profit = 0, 0
        for r in range(1, len(prices)):
            if prices[l] > prices[r]:
                l=r
            else:
                profit = max(profit, prices[r] - prices[l])

        return profit
        #2-pointers
        
        """#greedy approach if I were to maximize profit by selling multiple times
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]

        return profit
"""