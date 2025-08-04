#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        new_str_dic = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        sum_of_roman = new_str_dic[s[-1:]]
        ##うしろから見る
        for i in range(len(s)-2, -1, -1):
            if new_str_dic[s[i]] < new_str_dic[s[i+1]]:
                sum_of_roman -= new_str_dic[s[i]]
            else:
                sum_of_roman += new_str_dic[s[i]]
        return sum_of_roman
             
# @lc code=end

