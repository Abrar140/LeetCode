class Solution {
    public int maxOperations(int[] nums) {
      int score=nums[0]+nums[1];
      int count=1;

      for(int i=2; i<nums.length-1; i=i+2){
        if(score==(nums[i]+nums[i+1])){
            count++;
        }else{
            return count;
        }

      }

      return count;
        
    }
}