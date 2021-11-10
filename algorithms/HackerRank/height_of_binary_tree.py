'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''

def height(root):
    if root.left is None and root.right is None:
        return 0
    
    leftHeight, rightHeight = 0, 0
    if root.left: leftHeight = height(root.left)
    if root.right: rightHeight = height(root.right)

    return max(leftHeight, rightHeight) + 1

