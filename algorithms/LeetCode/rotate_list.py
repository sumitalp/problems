# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head: return None
        l = 1
        p = head
        while p.next:
            p = p.next
            l += 1
        k = k % l
        if l > k: p.next = head
        p = head
        for i in range(l-k-1):
            p = p.next
        res = p.next
        p.next = None
        return res

