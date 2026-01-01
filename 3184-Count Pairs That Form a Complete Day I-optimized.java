class Solution {
    public int countCompleteDayPairs(int[] hours) {
        int count=0;
        int[]  freq = new int[24];
        for (int h:hours){
            int remaindar= h%24;
            int complement= (24- remaindar)%24;
            count=count+ freq[complement];
            freq[remaindar]++;

        }
       
        return count;
        
    }
}