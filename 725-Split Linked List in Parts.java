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
    public ListNode[] splitListToParts(ListNode head, int k) {


    ListNode start= head;
    int count=0;
    while(start!=null){
        count++;
        start=start.next;
    }
    int base= count/k;
    int extra= count%k;
    start=head;

   ListNode[] ne= new ListNode[k];
    for(int i=0; i<k; i++){
        ne[i]=start;
        int time = base + (extra > 0 ? 1 : 0);
        extra--;

        for(int j=0; j<time-1 && start!=null; j++){
            start=start.next;
        }

        if(start!=null){
            ListNode next= start.next;
            start.next=null;
            start=next;
        }

        
    }

    return ne;
        
    }
}