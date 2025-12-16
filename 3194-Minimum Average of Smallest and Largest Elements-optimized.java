import java.util.*;

class Solution {
    public double minimumAverage(int[] nums) {

    Arrays.sort(nums);
    int left=0;
    int right=nums.length-1;
    double minmumaverage=Double.MAX_VALUE;    
    while(left<right){
        double calculatedaverage=(nums[left]+nums[right])/2.0;
        if (calculatedaverage<minmumaverage){
            minmumaverage=calculatedaverage;
        }
        left++;
        right--;        
    
    }
    return minmumaverage;        
    }
}