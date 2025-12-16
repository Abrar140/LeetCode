import java.util.*;

class Solution {
    public double minimumAverage(int[] nums) {

    Arrays.sort(nums);
    int left=0;
    int right=nums.length-1;
    List<Double> minmum=new ArrayList<>();
    
    while(left<right){
        minmum.add((nums[left]+nums[right])/2.0);
        left++;
        right--;        
    
    }
    Collections.sort(minmum);
    return minmum.get(0);        
    }
}