#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#

# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n_sorted = sorted(nums)
        for i in range(len(nums)+1):
            if i not in n_sorted:
                return i
        
# @lc code=end

