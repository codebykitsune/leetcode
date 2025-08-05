#
# @lc app=leetcode id=191 lang=python3
#
# [191] Number of 1 Bits
#

# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        n_bit = format(n, "b")
        arr = [int(digit) for digit in str(n_bit)]
        count = sum(arr)
        return count
        
# @lc code=end

