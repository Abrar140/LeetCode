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

 import java.util.*;
class Solution {
    public ListNode insertGreatestCommonDivisors(ListNode head) {
        ListNode current=head;
        if(head==null || head.next==null) return head;
        ListNode next=current.next;

        while(next!=null){
            
            int value= gcd(current.val, next.val);

            ListNode newNode= new ListNode(value);
            newNode.next=next;
            current.next=newNode;

            current=next;
                         next=next.next;
        }


        return head;
        
    }

    private int gcd(int a, int b){
        while(b!=0){
            int temp=b;
            b=a%b;
            a=temp;
        }

        return a;

    }
}