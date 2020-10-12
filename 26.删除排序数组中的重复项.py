#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        if length < 2:
            return length
        pos = 0
        for i in range(1, length):
            if nums[i] != nums[i-1]:
                pos += 1
                nums[pos] = nums[i]
        return pos + 1


# @lc code=end
