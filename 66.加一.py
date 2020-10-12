#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        plus = 1
        for index in range(len(digits)-1, -1, -1):
            val = digits[index] + plus
            digits[index] = val % 10
            plus = val // 10
        if plus:
            digits.insert(0, 1)
        return digits


# @lc code=end
