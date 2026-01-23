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
    public ListNode removeElements(ListNode head, int val) {

        ListNode previous=null;
        ListNode current=head;
        ListNode next=null;

        while(current!=null){

         if(current.val==val){
            next= current.next;
            if(previous==null){
                head=next;
            }else{
            previous.next=next;

            }
            
         }else{
         previous=current;
         }
         current=current.next;

        }

     return head;
        
    }
}