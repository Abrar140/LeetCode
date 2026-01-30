class Solution {
    public int pairSum(ListNode head) {

        ListNode fast = head;
        ListNode slow = head;

        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }

        ListNode prev = null;
        while (slow != null) {
            ListNode next = slow.next;
            slow.next = prev;
            prev = slow;
            slow = next;
        }

        int sum = 0;
        ListNode left = head;
        ListNode right = prev;

        while (right != null) {
            sum = Math.max(sum, left.val + right.val);
            left = left.next;
            right = right.next;
        }

        return sum;
    }
}
