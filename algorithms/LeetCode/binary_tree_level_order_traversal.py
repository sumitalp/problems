class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        from collections import deque
        
        if root is None:
            return list(list())
        result = list()
        q = deque()
        q.append(root)
        
        while q:
            node_count = len(q)
            result.append(list())
            while node_count > 0:
                node = q.popleft()
                result[-1].append(node.val)
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
                node_count -= 1
        
        return result

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        root.level = 0
        queue = [root]
        visited = []

        while queue:
            visited.append([])
            curr = queue.pop(0)
            visited[curr.level].append(curr.val)
            
            if curr.left:
                curr.left.level = curr.level + 1
                queue.append(curr.left)
            if curr.right:
                curr.right.level = curr.level + 1
                queue.append(curr.right)
                
        return [v for v in visited if v]
