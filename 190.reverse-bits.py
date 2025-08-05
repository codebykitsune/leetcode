#
# @lc app=leetcode id=190 lang=python3
#
# [190] Reverse Bits
#

# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        n_bit = format(n, '032b')
        n_reverse = n_bit[::-1]
        return int(n_reverse, 2)
        
# @lc code=end

