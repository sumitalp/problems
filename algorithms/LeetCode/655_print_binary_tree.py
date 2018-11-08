class Solution:
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        if not root:
            return
        
        from collections import deque
        
        def find_height(root):
            if not root:
                return 0
            
            return max(find_height(root.left), find_height(root.right)) + 1
        
        def num_of_nodes(root):
            return (2**find_height(root)) - 1
        
        q = deque()
        
        result = list()
        total_nodes = num_of_nodes(root)
        q.append((total_nodes//2, root))
        
        while q:
            node_count = len(q)
            result.append([""] * total_nodes)
            
            
            while node_count > 0:
                pos, curr = q.popleft()
                # if pos >= total_nodes: 
                #     pos = total_nodes - 1
                # if pos < 0:
                #     pos = 0
                    
                result[-1][pos] = str(curr.val)
                node_count -= 1
                
                if curr.left: 
                    q.append((max(0,pos//2),curr.left))
                if curr.right: 
                    q.append((min(pos+pos//2+1, total_nodes-1),curr.right))
                
        return result


class Solution1:
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        def depth(root):
            if not root:
                return 0
            return max(depth(root.left), depth(root.right)) + 1
        
        def helper(node, d, pos):
            self.res[-d-1][pos] = str(node.val)
            if node.left:
                helper(node.left, d-1, pos-2**(d-1))
            if node.right:
                helper(node.right, d-1, pos+2**(d-1))
        
        if not root:
            return ['']
        d = depth(root)
        self.res = [[''] * (2**d-1) for _ in range(d)]
        helper(root, d-1, 2**(d-1)-1)
        return self.res

