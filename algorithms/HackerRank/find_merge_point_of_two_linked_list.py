#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the findMergeNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
'''
    Using the difference in node counts)

    Get the count of the nodes in the first list, let the count be c1.
    Get the count of the nodes in the second list, let the count be c2.
    Get the difference of counts d = abs(c1 – c2)
    Now traverse the bigger list from the first node to d nodes so that from here onwards both the lists have an equal no of nodes
    Then we can traverse both lists in parallel till we come across a common node. (Note that getting a common node is done by comparing the address of the nodes)
    '''
def findMergeNode(head1, head2):
    c1 = countNode(head1)
    c2 = countNode(head2)
    d = abs(c1-c2)
    
    if c1>c2:
        return getIntersectionPoint(d, head1, head2)
    else:
        return getIntersectionPoint(d, head2, head1)
        

def getIntersectionPoint(d, h1, h2):
    cur1 = h1
    cur2 = h2
    
    for _ in range(d):
        if cur1:
            cur1 = cur1.next
        else:
            return
        
    while cur1 and cur2:
        if id(cur1) == id(cur2):
            return cur1.data
        cur1 =cur1.next
        cur2 = cur2.next

def countNode(head):
    count = 0
    cur = head
    while cur:
        count += 1
        cur = cur.next
    return count

