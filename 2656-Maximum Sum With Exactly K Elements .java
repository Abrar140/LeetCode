class Solution {
    public int maximizeSum(int[] nums, int k) {
        int maxVal=0;
        for(int m:nums){
            maxVal=Math.max(maxVal, m);
        }

      return k * maxVal + (k * (k - 1)) / 2  ;      
    }
}