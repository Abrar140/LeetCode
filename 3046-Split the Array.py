class Solution {
    public boolean isPossibleToSplit(int[] nums) {

        HashMap<Integer, Integer> map = new HashMap<>();
        for (int i=0; i<nums.length; i++){
            int key=nums[i];
            if(map.containsKey(key)){
             if(map.get(key)==2){
                return false;
             }
             map.put(key, map.get(key)+1);

            }else{
                map.put(key,1);
            }
        }
    return true;
        
    }
}