class Solution {
    public int longestPalindrome(String s) {
        int[] freq= new int[52];
        for(char c: s.toCharArray()){

            if(c-'a'>=0){
                freq[c-'a']++;
            }else{
            freq[c - 'A' + 26]++;
            }
        }
        int count=0;
        boolean odd= false;

        for(int i: freq){
            if(i%2==0){
                count=count+i;
            }else{
                odd=true;
                   count=count+i-1;
            }

        }

        return  odd? count+1: count;
        
    }
}