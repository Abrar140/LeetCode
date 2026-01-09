class Solution {
    public int minMoves(int[] nums) {
        int max=0;
        for(int n:nums){
            max=Math.max(max,n);
        }
        int sum=0;
          for(int n:nums){
            sum=sum+(max-n);
        }
        
        return sum;
    }
}