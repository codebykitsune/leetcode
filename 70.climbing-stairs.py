#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        F1 = 1
        F2 = 1
        for i in range(n-1):
            Fn = F1
            F1 = F1 + F2
            F2 = Fn
        return F1

        
# @lc code=end

