"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
# Recursive
def rec(node,right_node):
    if node:
        node.next = right_node
        rec(node.left,node.right)
        if right_node:
            rec(node.right,right_node.left)
        else:
            rec(node.right,None)
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        rec(root,None)
        return root


# Iterative

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        cur = [root]
        while len(cur) > 0:
            cur = [child for parent in cur if parent for child in [parent.left,parent.right]]

            last = None
            for ele in cur:
                if last != None:
                    last.next = ele
                last = ele
        
        return root
        