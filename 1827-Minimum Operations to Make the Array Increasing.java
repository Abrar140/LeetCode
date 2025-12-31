class Solution {
    public int minOperations(int[] nums) {
        int operations=0;
        
        for(int i=1; i<nums.length; i++){

            if(nums[i-1]>=nums[i]){
                int value=nums[i];
                nums[i]= nums[i-1]+1;
                operations=operations+nums[i]-value;
            }

        }       
        return operations;
    }
}