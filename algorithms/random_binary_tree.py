# Please implement a program that lists the nodes of a random binary tree by nodes at the same depth.

class Node:

    __slots__ = ['key', 'values', 'left', 'right']
    
    def __init__(self, key, value):
        self.key = key
        self.values = [value]
        self.left = None
        self.right = None


    def children_count(self):
        return int(self.left is not None) + int(self.right is not None)


    def is_leaf(self):
        return self.left is None and self.right is None


    def make_leaf(self):
        self.left = self.right = None

        return self


    def get_key(self):
        return self.key


    def get_value(self):
        return self.values[0]


    def get_values(self):
        return self.values


    def add_value(self, value):
        self.values.append(value)


    def has_value(self, value):
        return value in self.values
    

    def is_parent(self, child):
        return self.left is child or self.right is child


    def replace_child(self, child, new_node):
        if self.left is child:
            self.left = new_node
        elif self.right is child:
            self.right = new_node
        else:
            raise ValueError('replace_child: not a child')


    def other_child(self, child):
        if self.left is child:
            return self.right
        elif self.right is child:
            return self.left
        else:
            raise ValueError('other_child: not a child')


    def validate(self):
        if self.left:
            assert self.left.key < self.key, 'left child has key greater or equal'

        if self.right:
            assert self.right.key > self.key, 'right child has key less or equal'


class Tree(object):
    def __init__(self):
        self.root = None


    def insert(self, key, value):
        if self.root is None:
            self.root = Node(key, value)
            return self.root

        node = self.root
        while True:
            if key < node.get_key():
                if node.left:
                    node = node.left
                else:
                    leaf = Node(key, value)
                    node.left = leaf
                    return leaf
            elif key > node.get_key():
                if node.right:
                    node = node.right
                else:
                    leaf = Node(key, value)
                    node.right = leaf
                    return leaf
            else:
                if not node.has_value(value):
                    node.add_value(value)

                return node

    def find(self, key):
        node = self.root
        while node:
            if key == node.get_key():
                return node

            if key < node.get_key():
                node = node.left
            else:
                node = node.right


    def iter(self, node=None):
        if node is None:
            node = self.root

        queue = [(node, 0)]

        while queue:
            node, depth = queue.pop()
            if node is None:
                continue

            yield node, depth

            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))

if __name__ == '__main__':
    data = [
        (1, 'cat'),
        (8, 'dog'),
        (3, 'tree'),
        (10, 'sky'),
        (7, 'river'),
        (2, 'butterfly'),
        (5, 'bird'),
        (4, 'rock'),
        (6, 'mountain'),
        (10, 'cloud'),
    ]

    t = Tree()
    for key, value in data:
        t.insert(key, value)

    for key, value in data:
        node = t.find(key)
        assert node is not None
        assert node.has_value(value)

    assert t.find(99) is None
