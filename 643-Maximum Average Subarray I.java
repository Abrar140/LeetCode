class Solution {
    public double findMaxAverage(int[] nums, int k) {
        
        double maximumaverage=0.0;
        int Sum=0;

        for(int i=0; i<k; i++){
            Sum=Sum+nums[i];
        }
        maximumaverage= (double)Sum/k;
        for(int i=0;i<nums.length-k; i++){
            double average=0.0;
            Sum=Sum-nums[i]+nums[k+i];
            average=(double)Sum/k;
            if (average>maximumaverage){
                maximumaverage= average;
            }

        }
        return maximumaverage;
    }
}