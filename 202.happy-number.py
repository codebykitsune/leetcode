#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        new_n_set = set()
        while True:
            new_n = 0
            n_str = str(n)
            for j in range(len(n_str)):
                new_n += int(n_str[j])**2
            n = new_n
            if n in new_n_set:
                return False
            elif n == 1:
                return True
            new_n_set.add(n)

        
# @lc code=end

