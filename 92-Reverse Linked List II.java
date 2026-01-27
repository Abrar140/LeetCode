/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseBetween(ListNode head, int left, int right) {
     
    if (head == null || left == right) return head;

     ListNode l=head;
     ListNode lp=null;
     for(int i=1; i<left; i++){
        lp=l;
        l=l.next;
     }

     ListNode prev=null;
     ListNode next= l;

      for(int i=0; i<=right-left; i++){
        ListNode temp= next.next;
        next.next=prev;
        prev=next;
        next= temp;
     }
     ListNode tail = l;

if (lp != null) {
    lp.next = prev;
} else {
    head = prev;
}

tail.next = next;
 return head;
        
    }
}