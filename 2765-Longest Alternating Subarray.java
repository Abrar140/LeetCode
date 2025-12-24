class Solution {
    public int alternatingSubarray(int[] nums) {
        int max=-1;
        int count=1;
        boolean expectdec=false;
        for(int i=0; i<nums.length-1; i++){
            if(count==1){
                if(nums[i+1]==nums[i]+1){
                count=2;
                expectdec=true;
                max=Math.max(max,count);
              
                }
            }else{
            if(expectdec  &&  nums[i+1]==nums[i]-1  ){
            count++;
                           max=Math.max(max,count);

            expectdec=false;
            }
            else if(!expectdec  &&  nums[i+1]==nums[i]+1 ){
             count++;
                           max=Math.max(max,count);
                                       expectdec=true;


            }
            else{

            if (nums[i + 1] == nums[i] + 1) {
                        count = 2;
                        expectdec = true;
                        max = Math.max(max, count);
                    } else {
                        count = 1;
                        expectdec = false;
                    }
            }
            }
        }
        return max;
    }
}




