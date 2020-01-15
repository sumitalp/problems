# Tree - Practice lowest common ancestor

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Best Solution
class Solution:
    
    #Iterative using DFS - Not working properly
    # def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    #     if not root: return None
    #     q = []
    #     q.append(root)
    #     prev = root
    #     found = False
    #     while q or cur:
    #         if not cur.left:
    #             cur = q.pop()
    #             if cur.val == p.val or cur.val==q.val:
    #                 if found:return cur
    #                 found = True
    #             cur = cur.right
    #             q.append(cur)
    #         else:
    #             cur = cur.left
    #             q.append(cur)
    #     return None
    
    
    #Recursive
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or not p or not q: return None
        if root.val == p.val or root.val==q.val:
            return root
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)
        if not left: return right
        if not right: return left
        return root


# My Solution
class Solution1:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root: return None
        self.pathDict = {}
        path1 = list()
        path2 = list()
        
        self.getPath(root, path1, p)
        self.getPath(root, path2, q)
        
        intersection = -1
        i, j = 0, 0
        while i != len(path1) or j != len(path2):
            if i==j and i < len(path1) and j < len(path2) and path1[i]==path2[j]:
                i += 1
                j += 1
            else:
                intersection = j - 1
                break
                
        return self.pathDict[path1[intersection]]
        
    # Function to check if there is a path from root  
    # to the given node. It also populates  
    # 'arr' with the given path  
    def getPath(self, root: 'TreeNode', rarr: list, x: 'TreeNode'): 

        # if root is NULL  
        # there is no path  
        if not root: 
            return False

        # push the node's value in 'arr'  
        rarr.append(root.val)
        self.pathDict[root.val] = root

        # if it is the required node  
        # return true  
        if root.val == x.val: 
            return True

        # else check whether the required node lies  
        # in the left subtree or right subtree of  
        # the current node  
        if self.getPath(root.left, rarr, x) or self.getPath(root.right, rarr, x): 
            return True

        # required node does not lie either in the  
        # left or right subtree of the current node  
        # Thus, remove current node's value from  
        # 'arr'and then return false  
        rarr.pop() 
        return False