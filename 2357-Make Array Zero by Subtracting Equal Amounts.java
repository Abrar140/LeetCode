class Solution {
    public int minimumOperations(int[] nums) {
        Set<Integer> set= new HashSet<>();

        for(int n:nums){
            if(n!=0 && !set.contains(n)){
                set.add(n);
            }
        }

        return set.size();
        
    }
}