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

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
       
Approach:
1. Find a path from the root to n1 and store it in a vector or array. 
2. Find a path from the root to n2 and store it in another vector or array. 
3. Traverse both paths till the values in arrays are the same. Return the common element just before the mismatch. 
'''
# Time complexity: O(n)


def lca(root, v1, v2):
  def find_path(r, p, n):
    if not r: return False
    # Append the root
    p.append(r)
    
    if r.info == n:
        return True
    
    # Check if k is found in left or right sub-tree
    if (r.left and find_path(r.left, p, n)) or (r.right and find_path(r.right, p, n)):
        return True
 
    # If not present in subtree rooted with root, remove
    # root from path and return False
 
    p.pop()
    return False

  p1 = []
  p2 = []
  
  if not find_path(root, p1, v1) or not find_path(root, p2, v2):
    return -1

  i = 0
  while i < len(p1) and i < len(p2):
    if p1[i].info != p2[i].info:
        break
    i += 1
        
  return p1[i-1]

tree = BinarySearchTree()
