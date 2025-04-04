# ID: 226
# Title: Invert Binary Tree
# Link: https://leetcode.com/problems/invert-binary-tree/
# Difficulty: Easy
# Tags: Tree, Depth-First Search, Breadth-First Search, Binary Tree
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        root.left, root.right = self.invertTree(
            root.right), self.invertTree(root.left)
        return root

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        s = [root]
        while s:
            curr = s.pop()
            curr.left, curr.right = curr.right, curr.left
            curr.left and s.append(curr.left)
            curr.right and s.append(curr.right)
        return root
