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
    public ListNode sortList(ListNode head) {
        ListNode dummy= new ListNode(0);
        ListNode tail= dummy;
        
        while(head!=null){
            ListNode next= head;
            ListNode prevmin=null;
            ListNode prev=null;
            ListNode minm=null;

            while( next!=null){
                if(       minm == null ||next.val<minm.val){
                    //set min and its previous
                    minm=next;
                    prevmin=prev;
                  
                }
                prev=next;
                next=next.next;

            }
            //remove from orignal
            if(prevmin!=null){
               prevmin.next=minm.next;

            }else{
                head = head.next;
            }
            
            tail.next = minm;
            tail = tail.next;
            tail.next=null; 

        }

        return dummy.next;
    }
}

      

