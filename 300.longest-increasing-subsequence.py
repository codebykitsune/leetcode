#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ##動的計画法 Dynamic Programming
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[j] + 1
                    if dp[i] < dp[j] + 1:
                        dp[i] = dp[j] + 1
        return max(dp)
            
# @lc code=end

