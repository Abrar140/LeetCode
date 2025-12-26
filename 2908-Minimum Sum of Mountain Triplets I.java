class Solution {
    public int minimumSum(int[] nums) {
     
     int minSum=Integer.MAX_VALUE;

     for(int i=0; i<nums.length-2; i++){
         for(int j=i+1; j<nums.length-1; j++){
                 for(int k=j+1; k<nums.length; k++){
                   if(nums[i]<nums[j] && nums[k]<nums[j]){
                  int thisSum= nums[i]+nums[j] + nums[k];
                   minSum=Math.min(minSum,thisSum);
                 }

         }
      
        }
     }
     return minSum== 2147483647? -1: minSum;
        
    }
}