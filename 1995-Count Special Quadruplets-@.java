class Solution {
    public int countQuadruplets(int[] nums) {
        int n = nums.length;
        int count = 0;

        for(int k=n-2; k>=2; k--){
            Map<Integer, Integer> map = new HashMap<>();

            for(int m=k+1; m<n; m++){
                int diff = nums[m] - nums[k];
                map.put(diff, map.getOrDefault(diff, 0) + 1);
            }
             for (int i = 0; i < k; i++) {
                for (int j = i + 1; j < k; j++) {
                    int sum = nums[i] + nums[j];
                    count += map.getOrDefault(sum, 0);
                }
            }
        }    
        
        return count;
    }
}
