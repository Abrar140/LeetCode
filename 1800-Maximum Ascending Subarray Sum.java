class Solution {
    public int maxAscendingSum(int[] nums) {

        int maxSum=nums[0];
       int j=1;
       int  Sum=nums[0];
        while(j<nums.length){

         if(nums[j]> nums[j-1]){
            Sum= Sum+nums[j];
            maxSum= Math.max(maxSum, Sum);
         }else if(nums[j]<=nums[j-1]){
            Sum=nums[j];
         }
         j++;

        }

        return maxSum;
    }
}