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
    public ListNode mergeNodes(ListNode head) {
        ListNode previous=head;
        ListNode current=head.next;
        int Sum=0;

        while(current!=null){
            if(current.val==0){
                current.val=Sum;
                previous=current;
                Sum=0;

            }else{
                Sum=Sum+current.val;
                previous.next=current.next;
            }

            current=current.next;
        }
        return head.next;
        
    }
}