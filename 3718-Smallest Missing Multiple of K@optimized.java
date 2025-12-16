class Solution {
    public int missingMultiple(int[] nums, int k) {

        
        
        int num=1;
        while(num>0){
        boolean found=false;
        for(int n:nums){
            if(n==num*k){
                found=true;
                break;
            }
        }
        if (!found){
            return num*k;
        }

          
            num++;

        }
        return -1;
    }
}