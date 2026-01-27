class Solution {

    public int digitSum(int n){
        int Sum=0;
        n = Math.abs(n);
        while(n>0){
            Sum= Sum+ n%10;
            n=n/10;

        }
        return Sum;
    }

    public int minElement(int[] nums) {

        for(int i=0; i<nums.length; i++){
            nums[i]= digitSum(nums[i]);
        }

        int min= nums[0];
        for(int n: nums){
            min=Math.min(min,n);
        }

        return min;
        
    }
}