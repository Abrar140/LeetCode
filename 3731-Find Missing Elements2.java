class Solution {
    public List<Integer> findMissingElements(int[] nums) {

        Arrays.sort(nums);
        List<Integer> missing= new LinkedList<>();
        
        for(int i=0; i<nums.length-1; i++){
            if(nums[i+1] != nums[i]+1){
                int  word=nums[i]+1;
                while(word<nums[i+1]){
                    missing.add(word++);

                }
            }
        }

       
        return missing;
        
    }
}