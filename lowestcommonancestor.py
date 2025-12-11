# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """LeetCode 236. Lowest Common Ancestor of a Binary Tree"""
        lca, pfound, qfound = Solution.explore(root, p, q, False, False, False)
        return lca

    
    def explore(node, p, q, pfound, qfound, indescent):
        if node is None:
            return None, pfound, qfound
        indescent, pfound, qfound = Solution.get_descent(node, indescent, p, q, pfound, qfound)
        if indescent:
            return Solution.compute_descent_case(node, p, q, pfound, qfound, indescent)
        return Solution.compute_lca_case(node, p, q, pfound, qfound, indescent)
            
        
    
    def get_descent(node, indescent, p, q, pfound, qfound):
        if indescent:
            return True, pfound, qfound
        if node.val == p.val:
            pfound = True
            indescent = True
        elif node.val == q.val:
            qfound = True
            indescent = True
        return indescent, pfound, qfound
    
    def compute_lca_case(node, p, q, pfound, qfound, indescent):
        pos1, pfound1, qfound1 = Solution.explore(node.left, p, q, pfound, qfound, indescent)
        pos2, pfound2, qfound2 = Solution.explore(node.right, p, q, pfound, qfound, indescent)
        if pos1 is not None:
            return pos1, pfound1, qfound1
        if pos2 is not None:
            return pos2, pfound2, qfound2
        pfound = pfound1 or pfound2
        qfound = qfound1 or qfound2
        is_lca = pfound and qfound
        if is_lca:
            return node, pfound, qfound
        return None, pfound, qfound
    
    def compute_descent_case(node, p, q, pfound, qfound, indescent):
        if node.val == p.val:
            if qfound:
                return q, pfound, qfound
            pfound = True
        elif node.val == q.val:
            if pfound:
                return p, pfound, qfound
            qfound = True
        pos1, pfound1, qfound1 = Solution.explore(node.left, p, q, pfound, qfound, indescent)
        pos2, pfound2, qfound2 = Solution.explore(node.right, p, q, pfound, qfound, indescent)
        if pos1 is not None:
            return pos1, pfound1, qfound1
        elif pos2 is not None:
            return pos2, pfound2, qfound2
        return None, pfound, qfound