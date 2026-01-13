class Solution {
    public boolean isGood(int[] nums) {
        int max=-1;
        for(int n: nums){
            max=Math.max(max, n);
        }
        if(nums.length!=max+1){
            return false;
        }
        int[] freq= new int[max+1];
         for(int n: nums){
            freq[n]++;
        }
        if(freq[max]!=2){
            return false;
        }

        for(int f=1; f<max; f++){
            if(freq[f]!=1){
                return false;
            }
        }



        return true;
        
    }
}