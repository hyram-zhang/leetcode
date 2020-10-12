#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
from typing import List, Generator


class Solution:

    def generateParenthesis(self, n: int) -> List[str]:
        return list(self._generate(0, 0, n, ''))

    def _generate(self, left: int, right: int, n: int, s: string) -> Generator:
        if left == right == n:
            yield s
        if left < n:
            yield from self._generate(left+1, right, n, f"{s}(")
        if left > right:
            yield from self._generate(left, right+1, n, f"{s})")


class Solution:
    @lru_cache(None)
    def generateParenthesis(self, n: int) -> List[str]:
        def _generate():
            if not n:
                yield ''
            for i in range(n):
                for part_a in self.generateParenthesis(i):
                    for part_b in self.generateParenthesis(n-1-i):
                        yield f"({part_a}){part_b}"
        return list(_generate())

# @lc code=end
