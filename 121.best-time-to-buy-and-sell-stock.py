#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        max_price = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                price = prices[right] - prices[left]
                max_price = max(max_price, price)
            else:
                #右に進む
                left = right
            right += 1
            
        return max_price
            
        
# @lc code=end

