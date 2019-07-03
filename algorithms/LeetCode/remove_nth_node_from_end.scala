// Leetcode: 19. Remove Nth Node From End of List

/**
 * Definition for singly-linked list.
 * class ListNode(var _x: Int = 0) {
 *   var next: ListNode = null
 *   var x: Int = _x
 * }
 */
import scala.util.control.Breaks._

object Solution {
    def removeNthFromEnd(head: ListNode, n: Int): ListNode = {
        var newHead: ListNode = head;
        var temp: ListNode = newHead;
        var sLast: ListNode = null;
        var last: ListNode = null;
        var tailList: ListNode = null;
        var counter: Int = 1;
        
        breakable{
            while(counter<=n){
                if(temp != null && temp.next != null){
                    while(temp.next != null){
                        sLast = temp;
                        last = temp.next;
                        temp = temp.next;
                    }
                    sLast.next = null;
                } else {
                    sLast = null;
                }

                if(counter==n){
                    if(sLast != null){
                        sLast.next = tailList;
                    } else {
                        return tailList;
                    }
                    break;
                }else{
                    if(tailList == null){
                        tailList = last;
                    } else {
                        last.next = tailList;
                        tailList = last;
                    }
                    temp = newHead;
                }
                counter += 1;
            }
        }
        
        return newHead;
    }
}
