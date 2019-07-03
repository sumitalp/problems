# Please implement a program that lists the nodes of a random binary tree by nodes at the same depth.

from collections import deque

class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def iter_layers(self):
        q = deque()
        q.append(self)

        def layer_iterator(layer_size):
            for i in range(layer_size):
                n = q.popleft()
                if n.left: q.append(n.left)
                if n.right: q.append(n.right)
                yield n.value

        while (q):
            yield layer_iterator(len(q))

    def print_layer(self):
        for layer in self.iter_layers():
            print( ' '.join( [str(v) for v in layer] ) )


if __name__ == '__main__':
    t = Node(1, Node(2, Node(4, Node(7))), Node(3, Node(5), Node(6)))

    t.print_layer()
