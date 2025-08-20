#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#

# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        left, right = 0, len(matrix) - 1
        while left < right:
            for i in range(left, right-1):
                top, bottom = left, right

                #save the top left
                topLeft = matrix[top][left + i]

                #move bottom Left into top Left
                matrix[top][left + i] = matrix[bottom - i][left]

                #move bottom right into bottom left
                matrix[bottom - i][left] = matrix[bottom][right - i]

                #move top right into bottom right
                matrix[bottom][right - i] = matrix[top + i][right]

                #move top left into top right
                matrix[top + i][right] = topLeft
            right -= 1
            left += 1

        
# @lc code=end

