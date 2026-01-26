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
    public ListNode rotateRight(ListNode head, int k) {
        if(head==null || head.next==null || k==0)  return head;
        int total=1;
        ListNode current=head;
        while(current.next!=null){
            total++;
            current=current.next;
        }
        current.next= head;

        k = k % total;
        if (k == 0) {
            current.next = null;
            return head;
        }

         current=head;
       
        for(int i=1; i<total-k; i++) {
          
            current=current.next;

        }
        ListNode newnode= current.next;
        current.next=null;
        head=newnode;

        return head;
        
    }
}