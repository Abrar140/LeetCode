class Solution {
    public int findMaxK(int[] nums) {
        int max= Integer.MIN_VALUE;
        Set<Integer> set= new HashSet<>();
        for(int n: nums){
            int  n1=n*-1;
            if(set.contains(n1) && Math.abs(n)>max){
                max= Math.abs(n);
                
            }else{
                set.add(n);
            }
        }

        return max== Integer.MIN_VALUE? -1: max;
        
    }
}