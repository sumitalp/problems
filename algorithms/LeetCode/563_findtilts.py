# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.tilt = 0

        if root:
            self.dfs(root)
        
        return self.tilt
    
    def dfs(self, root):
        if not root:
            return 0
        
        left_sum = self.dfs(root.left)    
        right_sum = self.dfs(root.right)
        
        self.tilt += abs(left_sum - right_sum)
        return left_sum + right_sum + root.val

