# ID: 235
# Title: Lowest Common Ancestor of a Binary Search Tree
# Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
# Difficulty: Medium
# Tags: Tree, Depth-First Search, Binary Search Tree, Binary Tree
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        result = None
        for p_node, q_node in zip(self.dfs(root, p), self.dfs(root, q)):
            if p_node == q_node:
                result = p_node
            else:
                break
        return result

    def dfs(self, root: 'TreeNode', target: 'TreeNode') -> Optional[List['TreeNode']]:
        if root == target:
            return [root]
        if root is None:
            return None
        l, r = self.dfs(root.left, target), self.dfs(root.right, target)
        if r:
            return [root] + r
        else:
            return None if not l else [root] + l

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                return root
