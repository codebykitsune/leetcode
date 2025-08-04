#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        F1 = 1
        F2 = 2
        for _ in range(3, n+ 1):
            Fn = F1 + F2
            F1 = F2
            F2 = Fn
        return F2

        
# @lc code=end

