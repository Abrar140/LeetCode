class Solution {
    public int maxNumberOfBalloons(String text) {
        int[] freq= new int [26];

        for(char c: text.toCharArray()){
            freq[c-'a']++;
        }
        String b= "balloon";

        int[] freqb= new int [26];

        for(char c: b.toCharArray()){
            freqb[c-'a']++;
        }
        
        int count=Integer.MAX_VALUE;
        for(int i=0; i<freq.length; i++){
            if(freqb[i]!=0){
                count=Math.min(count, freq[i]/freqb[i]);
            }
        }

     return count;
        
    }
}