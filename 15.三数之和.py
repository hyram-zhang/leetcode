#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
from types import resolve_bases


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        length = len(nums)
        for x in range(length):
            for y in range(x+1, length):
                for z in range(y+1, length):
                    if not nums[x]+nums[y]+nums[z]:
                        alist = [nums[x], nums[y], nums[z]]
                        alist.sort()
                        if alist not in result:
                            result.append(alist)
        result.sort()
        return result


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        if length < 3:
            return []
        nums.sort()
        result = []
        adict = dict()
        for i in range(length):
            if nums[i] > 0:
                return result
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i+1
            right = length - 1
            while left < right:
                num_sum = nums[i] + nums[left] + nums[right]
                if not num_sum:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif num_sum > 0:
                    right -= 1
                else:
                    left += 1
        return result


# @lc code=end
