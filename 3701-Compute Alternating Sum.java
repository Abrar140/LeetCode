class Solution {
    public int alternatingSum(int[] nums) {
        int output=0;
        for(int i=0;i<nums.length;i++){
           if(i%2==0){
            output=output+nums[i];
           }else{
            output=output-nums[i];
           }
        }

        return output;
        
    }
}



/*int sum = 0, sign = 1;
for (int num : nums) {
    sum += sign * num;
    sign *= -1;
}*/
