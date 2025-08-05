#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#

# @lc code=start
class Solution:
    def countBits(self, n: int) -> List[int]:
        arr =[]
        for i in range(n+1):
            binary_string = format(i, "b")
            count = binary_string.count("1")
            arr.append(count)
        return arr
        
# @lc code=end

