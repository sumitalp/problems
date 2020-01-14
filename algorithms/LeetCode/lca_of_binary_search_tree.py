# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root: return 
        
        if p.val < root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
            
        if p.val > root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
            
        return root


# Testcase
# [12,5,1,6,4,0,8,null,null,3,2]
# 5
# 4