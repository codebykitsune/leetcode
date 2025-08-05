#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price_so_far = prices[0]
        max_profit_so_far = 0

        for i in range(1,len(prices)):
            if prices[i] <= min_price_so_far:
                min_price_so_far = prices[i]
            
            #その日までの利益
            todays_profit = prices[i] - min_price_so_far

            if todays_profit > max_profit_so_far:
                max_profit_so_far = todays_profit
    
    
        return max_profit_so_far
            
        
# @lc code=end

