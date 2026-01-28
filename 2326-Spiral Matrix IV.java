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
    public int[][] spiralMatrix(int m, int n, ListNode head) {

        int[][] mat= new int [m][n];

         for (int i = 0; i < m; i++) {
            Arrays.fill(mat[i], -1);
        }
        int top = 0, bottom = m - 1;
        int left = 0, right = n - 1;


        int i=0; 
        int  j=0;
        int dir=0;

        while (head!=null){

            mat[i][j]= head.val;
            head=head.next;
        if (dir == 0) { 
                if (j < right) j++;
                else {
                    dir = 1;
                    top++;
                    i++;
                }
            } 
            else if (dir == 1) { 
                if (i < bottom) i++;
                else {
                    dir = 2;
                    right--;
                    j--;
                }
            } 
            else if (dir == 2) { 
                if (j > left) j--;
                else {
                    dir = 3;
                    bottom--;
                    i--;
                }
            } 
            else { 
                if (i > top) i--;
                else {
                    dir = 0;
                    left++;
                    j++;
                }
            }



        }
        return mat;
    }
}