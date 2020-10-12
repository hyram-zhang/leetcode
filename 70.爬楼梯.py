#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    result = {1: 1, 2: 2}

    def climbStairs(self, n: int) -> int:
        if n not in self.result:
            self.result[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.result[n]


class Solution:
    @functools.lru_cache
    def climbStairs(self, n: int) -> int:
        if n in (1, 2):
            return n
        return self.climbStairs(n-1) + self.climbStairs(n-2)


class Solution:
    def climbStairs(self, n: int) -> int:
        result = {1: 1, 2: 2}
        for i in range(3, n+1):
            result[i] = result[i-1] + result[i-2]
        return result[n]


class Solution:
    def climbStairs(self, n: int) -> int:
        if n in (1, 2):
            return n
        a, b, = 1, 2
        for i in range(3, n+1):
            a, b = b, a+b
        return b


# @lc code=end
