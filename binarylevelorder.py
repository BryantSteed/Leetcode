# Definition for a binary tree node.
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """Leetcode 102: Binary Tree Level Order Traversal"""
        if root is None:
            return []
        order = []
        self.dfs(order, root, 0)
        return order
    
    def dfs(self, order: List[int], node: TreeNode, level: int):
        if node is None:
            return
        if len(order) <= level:
            order.append([])
        order[level].append(node.val)
        self.dfs(order, node.left, level+1)
        self.dfs(order, node.right, level+1)
        