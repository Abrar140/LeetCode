/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {

        while(headA!=null){
            ListNode start=headB;
            while(start!=null){
                if(headA==start){
                    return headA;
                }
                start=start.next;

            }
            headA=headA.next;

            
        }



        return null;
    }
}