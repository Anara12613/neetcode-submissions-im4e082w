class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_price = 0
        left = 0
        
        for r in range(1,len(prices)):
            if prices[left]<prices[r]:
                profit = prices[r] - prices[left]
                max_price = max(max_price,profit)
            else:
                left =r
            
        return max_price


        