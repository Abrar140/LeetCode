class Solution {
    public int minimumSumSubarray(List<Integer> nums, int l, int r) {
        int minSum= Integer.MAX_VALUE;
         for(int size=l; size<=r; size++){
            int Sum=0;
            for(int i=0; i<size; i++){
                Sum=Sum+nums.get(i);
            }
            if(Sum>0){
                minSum=Math.min(minSum, Sum);
            }

            for(int i=size; i<nums.size(); i++){
                 Sum=Sum+nums.get(i)-nums.get(i-size);

                if(Sum>0){
                    minSum=Math.min(minSum, Sum);

                }

              
            }
         }


      
        return minSum == Integer.MAX_VALUE ? -1 : minSum;
        
    }
}