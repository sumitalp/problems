'''
1
    \
     2
      \
       5
      /  \
     3    6
      \
       4

Output: 1 2 5 6

Approach: We use vertical ordering
'''

class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def topView(root):
    def getVerticalOrder(root, hd, lvl, mapp):
        if root is None: return
        if hd not in mapp:
            mapp[hd] = [root.info, lvl]
        elif mapp[hd][1] > lvl:
            mapp[hd] = [root.info, lvl]
            
        getVerticalOrder(root.left, hd-1, lvl+1, mapp)
        getVerticalOrder(root.right, hd+1, lvl+1, mapp)
    
    vertical_map = dict()
    horizontal_distance = 0
    getVerticalOrder(root, horizontal_distance, 0, vertical_map)

    for m in sorted(vertical_map):
        print(vertical_map[m][0], end=" ")



tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

topView(tree.root)
