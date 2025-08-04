#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        plus = 1
        for i in range(len(digits)-1, -1,-1):
            sum_n = digits[i] + plus
            digits[i] = sum_n % 10
            if sum_n <10:
                plus = 0
                break
        if plus > 0:
            digits.insert(0,1)

        return digits
        


        
# @lc code=end

