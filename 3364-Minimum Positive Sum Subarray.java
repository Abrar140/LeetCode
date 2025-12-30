class Solution {
    public int minimumSumSubarray(List<Integer> nums, int l, int r) {
        int minSum= Integer.MAX_VALUE;
         for(int size=l; size<=r; size++){
            for(int i=0; i<=nums.size()-size; i++){
                int Sum=0;
                for(int j=i; j<i+size; j++){
                    Sum=Sum+nums.get(j);
                }

                  if(Sum<minSum && Sum>0){
            minSum=Sum;
        }

            }
         }


      
        return minSum == Integer.MAX_VALUE ? -1 : minSum;
        
    }
}