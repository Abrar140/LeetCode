class Solution {
    public boolean check(int[] nums) {
        int min=Integer.MAX_VALUE;
        int index=0;

        for(int i=nums.length-1; i>=0; i--){
            if(nums[i]<min){
                min=nums[i];
                index=i;
            }else if( nums[i]==min){
                if(i!=index-1){
                index= Math.max(index, i);

                }else{
                    index=i;
                }
            }
        }

        int start=0;
        int[] ne= new int[nums.length];
        for(int i=index; i<nums.length ; i++){
           ne[start++]=nums[i];
        }

        for(int i=0; i<index ; i++){
           ne[start++]=nums[i];
        }

         for(int i=0; i<ne.length-1 ; i++){
            if(ne[i]>ne[i+1]){
                return false;
            }
        }


        return true;
        
    }
}