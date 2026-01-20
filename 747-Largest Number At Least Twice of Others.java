class Solution {
    public int dominantIndex(int[] nums) {

        int maxIndex=0;
        int  max=0;

        for(int i=0; i<nums.length; i++){
            if(max<nums[i]){
                maxIndex=i;
                max=nums[i];
                
            }
        }

          for(int i=0; i<nums.length; i++){
            int dble= nums[i]*2;

            if(maxIndex!=i && max<dble){
                return -1;
                
            }
        }

        return maxIndex;
        
    }
}