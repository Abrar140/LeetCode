class Solution {
    public boolean isEven(int num){
        return num%2==0;
    }
    public int[] sortArrayByParity(int[] nums) {
        int left=0;
        int right=nums.length-1;
        while(left<right){
            if(isEven(nums[left])){
                left++;
            }else if(!isEven(nums[right])){
                right--;
            }else{
                int temp=nums[left];
                nums[left]=nums[right];
                nums[right]=temp;

                left++;
                right--;
            }
        }

        return nums;
        
    }
}