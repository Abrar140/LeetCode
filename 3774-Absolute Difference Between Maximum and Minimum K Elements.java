class Solution {
    public int absDifference(int[] nums, int k) {
        int Sum=0;
        Arrays.sort(nums);

        for(int i=nums.length-1; i>nums.length-1-k; i-- ){
            Sum=Sum+nums[i];
        }

        for(int i=0; i<k; i++){
            Sum=Sum-nums[i];
        }
        
        return Math.abs(Sum);
    }
}