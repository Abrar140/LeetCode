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
    public ListNode mergeInBetween(ListNode list1, int a, int b, ListNode list2) {
      
      ListNode current=list1;
      for(int i=0; i<a-1; i++){
        current=current.next;
      }
 
      ListNode next= current.next;

      current.next=list2;

       for(int i=a; i<b; i++){
        next=next.next;
      }
    
      while(list2.next!=null){
        list2=list2.next;
      }
      list2.next=next.next;
    return list1;
        
    }
}