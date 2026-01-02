class Solution {
    public boolean isEven(int n){
        return n%2==0;
    }
    public int[] sortArrayByParityII(int[] nums) {
        int left=0;
        int right=1;

        while(left<nums.length && right< nums.length){
            if(isEven(nums[left])){
                left+=2;
            }else  if(!isEven(nums[right])){
                right+=2;
            }else{

                 int temp= nums[left];
                nums[left]=nums[right];
                nums[right]=temp;
                left+=2;
                right+=2;
            }
               
   
        }
        return nums;
        
    }
}