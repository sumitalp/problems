// LeetCode: 61. Rotate List

/**
 * Definition for singly-linked list.
 * class ListNode(var _x: Int = 0) {
 *   var next: ListNode = null
 *   var x: Int = _x
 * }
 */
import scala.util.control.Breaks._

object Solution {
    def rotateRight(head: ListNode, k: Int): ListNode = {
        if(head == null || head.next == null){
            return head;
        }
        var temp_k = k;
        while(temp_k>100000){
            var q = temp_k / 100000;
            var r = temp_k % 100000;
            temp_k = q + r;
        }
        println(temp_k);
        var newHead: ListNode = head;
        var temp: ListNode = newHead;
        var counter = 0;
        var last: ListNode = null;
        var sLast: ListNode = null;
        breakable{
            while(counter <= temp_k){
                while(temp.next != null){
                    sLast = temp;
                    last = temp.next;
                    temp = temp.next;
                }
                

                if(counter == temp_k){
                    break;
                } else {
                    last.next = newHead;
                    newHead = last;
                    temp = newHead;
                    sLast.next = null;
                }
                counter += 1;
            }
        }
        
        return newHead;
    }
}
