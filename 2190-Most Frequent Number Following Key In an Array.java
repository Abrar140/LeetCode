class Solution {
    public int mostFrequent(int[] nums, int key) {
        
        int[] freq= new int[1001];
        for(int i=1; i<nums.length; i++){
            if(nums[i-1]==key){
                freq[nums[i]]++;
            }
        }

       int maxFreq = 0;
        int result = 0;

        for (int i = 0; i < freq.length; i++) {
            if (freq[i] > maxFreq) {
                maxFreq = freq[i];
                result = i;
            }
        }

        return result;
    }
}