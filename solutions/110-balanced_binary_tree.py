# ID: 110
# Title: Balanced Binary Tree
# Link: https://leetcode.com/problems/balanced-binary-tree/
# Difficulty: Easy
# Tags: Tree, Depth-First Search, Binary Tree
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.height(root) != -1

    def height(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        l_h, r_h = self.height(root.left), self.height(root.right)
        if l_h == -1 or r_h == -1 or abs(l_h - r_h) > 1:
            return -1
        return max(l_h, r_h) + 1
