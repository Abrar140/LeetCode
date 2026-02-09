/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int traverse(TreeNode root, int low, int high , int sum) {
if (root == null) return sum;

    if(root.val>=low && root.val<=high){
        sum=sum+root.val;

    }
    sum=traverse(root.left, low, high, sum);              
    sum=traverse(root.right, low, high, sum);              
    return sum;           
}
    public int rangeSumBST(TreeNode root, int low, int high) {

            return traverse(root, low, high, 0);   
    }
}