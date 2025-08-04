#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_list = set()
        if len(nums) == 2:
            return [0,1]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if target == nums[i] + nums[j] and i != j:
                    new_list.add(i)
                    new_list.add(j)
        return list(new_list)

        
# @lc code=end

