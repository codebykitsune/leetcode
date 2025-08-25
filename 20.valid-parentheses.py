#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_to_open = {")":"(", "}":"{", "]":"["}

        for c in s:
            if c in close_to_open:
                if stack and stack[-1] == close_to_open[c]:
                    stack.pop()
                else:
                    return False      
            else:
                stack.append(c)
        return True if not stack else False
        
# @lc code=end

