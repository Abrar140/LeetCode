class Solution {
    public int pivotIndex(int[] nums) {
      
       for(int i=0; i<nums.length; i++){
        int leftsum=0;
       int rightsum=0;
       int start=0;
       int end=i+1;
       while(start<i){
        leftsum=nums[start]+leftsum;
        start++;
       }

        while(end<nums.length){
        rightsum=nums[end]+rightsum;
        end++;
       }
       if(leftsum==rightsum){
        return i;
       }

       }
        return -1;
        
    }
}