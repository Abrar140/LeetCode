
class Solution {
    public int minOperations(int[] nums, int k) {
        Set<Integer> arr= new HashSet<>();
        for(int num:nums){
            if(num<k){
                return -1;
            }else if(num>k){
                arr.add(num);
            }
        }
        return arr.size();
    }
}