# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        visited = []
        if root:
            stack = [root]
            
            while root or len(stack) > 0:
                if root and root.left:
                    stack.append(root.left)
                    root = root.left
                else:
                    node = stack.pop()
                    visited.append(node.val)
                
                    if node.right:
                        stack.append(node.right)
                    root = node.right
                
        return visited