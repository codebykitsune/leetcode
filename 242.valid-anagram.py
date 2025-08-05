#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_new = sorted(s)
        t_new = sorted(t)
        return s_new == t_new

        
# @lc code=end

