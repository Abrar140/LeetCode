class Solution {
    public int[] maxKDistinct(int[] nums, int k) {

        Arrays.sort(nums);
        Set<Integer> Set = new HashSet<>();
        int [] re = new int[Math.min(nums.length, k)];
        int s=0;


        for(int i=nums.length-1; i>=0; i--){
            if(s==k){
                break;
            }
            if(!Set.contains(nums[i])){
               re[s++]=nums[i];
            Set.add(nums[i]);

            }
        }

       return Arrays.copyOf(re, s);
        
    }
}