class Solution {
    public int averageValue(int[] nums) {
        int count=0;
        int totalSum=0;
        for(int n:nums){
            if(n%6==0){
                count++;
                totalSum=totalSum+n;
            }
        }

        return count==0?0:totalSum/count;
        
    }
}