class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

def ReversePrint(head):
    if head is not None:
        ReversePrint(head.next)
        print(head.data)
