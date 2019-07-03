/**
 * Definition for singly-linked list.
 * class ListNode(var _x: Int = 0) {
 *   var next: ListNode = null
 *   var x: Int = _x
 * }
 */
object Solution {
    def mergeTwoLists(l1: ListNode, l2: ListNode): ListNode = {
        var head: ListNode = new ListNode();
        var curr: ListNode = head;
        var l3: ListNode = l1;
        var l4: ListNode = l2;
        
        while (l3 != null && l4 != null){
            if (l3.x < l4.x){
                curr.next = l3
                l3 = l3.next
            } else {
                curr.next = l4
                l4 = l4.next
            }
            curr = curr.next
        }
        
        if(l3==null){
            curr.next = l4;
        } else {
            curr.next = l3;
        }
        
        return head.next;
    }
}
