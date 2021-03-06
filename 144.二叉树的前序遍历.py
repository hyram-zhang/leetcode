#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def _preorderTraversal(root:TreeNode):
            if not root:
                return
            res.append(root.val)
            _preorderTraversal(root.left)
            _preorderTraversal(root.right)
        _preorderTraversal(root)
        return res

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack = [root]
        res = []
        while stack:
            root = stack.pop()
            res.append(root.val)
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)
        return res

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return res
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = []
        while root:
            res.append(root.val)
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)
            root = stack.pop() if stack else None
        return res


        
# @lc code=end

