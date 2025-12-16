class Solution {
    public int countPartitions(int[] nums) {
        int totalSum=0;
        for (int num:nums){
            totalSum=totalSum+num;
        }
        int leftSum=0;
        int partitionCount=0;
        for(int i=0; i<nums.length-1;i++){
            leftSum=leftSum+nums[i];
            int rightSum=totalSum-leftSum;
            if((leftSum-rightSum)%2==0){
                partitionCount++;
            }
        }
        return partitionCount;
    }
}