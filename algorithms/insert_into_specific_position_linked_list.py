"""
 Insert Node at a specific position in a linked list
 head input could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method. 
"""
class Node(object):
  def __init__(self, data=None, next_node=None):
      self.data = data
      self.next = next_node

def InsertNth(head, data, position):
    current = head
    count = 0
    
    if position == 0:
        return Node(data, current)
    
    while current.next and count < position-1:
        current = current.next
        count += 1
        
    node_at_position = current.next
    current.next = Node(data)
    current = current.next
    current.next = node_at_position
  
    return head


if __name__=='__main__':
    n = InsertNth(None,3,0)
    InsertNth(n,5,1)
    InsertNth(n,4,2)
    InsertNth(n,2,3)
    InsertNth(n,10,1)

    print(n.data)
    print(n.next.data)
    print(n.next.next.data)
    print(n.next.next.next.data)
    print(n.next.next.next.next.data)
